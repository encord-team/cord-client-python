#
# Copyright (c) 2020 Cord Technologies Limited
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

""" ``encord.client`` provides a simple Python client that allows you
to query project resources through the Encord API.

Here is a simple example for instantiating the client for a project
and obtaining project info:

.. test_blurb2.py code::

    from encord.client import EncordClient

    client = EncordClient.initialize('YourProjectID', 'YourAPIKey')
    client.get_project()

    Returns:
        Project: A project record instance. See Project ORM for details.

"""

from __future__ import annotations

import base64
import json
import logging
import os.path
import typing
import uuid
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Tuple, Union

import encord.exceptions
from encord.configs import ENCORD_DOMAIN, ApiKeyConfig, Config, EncordConfig
from encord.constants.model import AutomationModels
from encord.constants.string_constants import *
from encord.http.querier import Querier
from encord.http.utils import (
    CloudUploadSettings,
    upload_images_to_encord,
    upload_to_signed_url_list,
    upload_video_to_encord,
)
from encord.orm.api_key import ApiKeyMeta
from encord.orm.cloud_integration import CloudIntegration
from encord.orm.dataset import AddPrivateDataResponse
from encord.orm.dataset import Dataset as OrmDataset
from encord.orm.dataset import (
    DatasetData,
    Image,
    ImageGroup,
    ImageGroupOCR,
    Images,
    ReEncodeVideoTask,
    Video,
)
from encord.orm.label_log import LabelLog
from encord.orm.label_row import (
    AnnotationTaskStatus,
    LabelRow,
    LabelRowMetadata,
    LabelStatus,
    Review,
)
from encord.orm.labeling_algorithm import (
    BoundingBoxFittingParams,
    LabelingAlgorithm,
    ObjectInterpolationParams,
)
from encord.orm.model import (
    Model,
    ModelInferenceParams,
    ModelOperations,
    ModelRow,
    ModelTrainingParams,
)
from encord.orm.project import Project as OrmProject
from encord.orm.project import (
    ProjectCopy,
    ProjectCopyOptions,
    ProjectDataset,
    ProjectUsers,
)
from encord.project_ontology.classification_type import ClassificationType
from encord.project_ontology.object_type import ObjectShape
from encord.project_ontology.ontology import Ontology
from encord.utilities.client_utilities import parse_datetime
from encord.utilities.project_user import ProjectUser, ProjectUserRole

logger = logging.getLogger(__name__)


class EncordClient(object):
    """
    Encord client. Allows you to query db items associated
    with a project (e.g. label rows, datasets).
    """

    def __init__(self, querier: Querier, config: Config):
        self._querier = querier
        self._config: Config = config

    @staticmethod
    def initialise(
        resource_id: Optional[str] = None, api_key: Optional[str] = None, domain: str = ENCORD_DOMAIN
    ) -> Union[EncordClientProject, EncordClientDataset]:
        """
        Create and initialize a Encord client from a resource EntityId and API key.

        Args:
            resource_id: either of the following

                * A <project_hash>.
                  If ``None``, uses the ``ENCORD_PROJECT_ID`` environment variable.
                  The ``CORD_PROJECT_ID`` environment variable is supported for backwards compatibility.

                * A <dataset_hash>.
                  If ``None``, uses the ``ENCORD_DATASET_ID`` environment variable.
                  The ``CORD_DATASET_ID`` environment variable is supported for backwards compatibility.

            api_key: An API key.
                     If None, uses the ``ENCORD_API_KEY`` environment variable.
                     The ``CORD_API_KEY`` environment variable is supported for backwards compatibility.
            domain: The encord api-server domain.
                If None, the :obj:`encord.configs.ENCORD_DOMAIN` is used

        Returns:
            EncordClient: A Encord client instance.
        """
        config = EncordConfig(resource_id, api_key, domain=domain)
        return EncordClient.initialise_with_config(config)

    @staticmethod
    def initialise_with_config(config: ApiKeyConfig) -> Union[EncordClientProject, EncordClientDataset]:
        """
        Create and initialize a Encord client from a Encord config instance.

        Args:
            config: A Encord config instance.

        Returns:
            EncordClient: A Encord client instance.
        """
        querier = Querier(config)
        key_type = querier.basic_getter(ApiKeyMeta)
        resource_type = key_type.get("resource_type", None)

        if resource_type == TYPE_PROJECT:
            logger.info("Initialising Encord client for project using key: %s", key_type.get("title", ""))
            return EncordClientProject(querier, config)

        elif resource_type == TYPE_DATASET:
            logger.info("Initialising Encord client for dataset using key: %s", key_type.get("title", ""))
            return EncordClientDataset(querier, config)

        else:
            raise encord.exceptions.InitialisationError(
                message=f"API key [{config.api_key}] is not associated with a project or dataset"
            )

    def __getattr__(self, name):
        """Overriding __getattr__."""
        value = self.__dict__.get(name)
        if not value:
            self_type = type(self).__name__
            if self_type == "CordClientDataset" and name in EncordClientProject.__dict__.keys():
                raise encord.exceptions.EncordException(
                    message=("{} is implemented in Projects, not Datasets.".format(name))
                )
            elif self_type == "CordClientProject" and name in EncordClientDataset.__dict__.keys():
                raise encord.exceptions.EncordException(
                    message=("{} is implemented in Datasets, not Projects.".format(name))
                )
            elif name == "items":
                pass
            else:
                raise encord.exceptions.EncordException(message="{} is not implemented.".format(name))
        return value

    def get_cloud_integrations(self) -> List[CloudIntegration]:
        return self._querier.get_multiple(CloudIntegration)


CordClient = EncordClient


class EncordClientDataset(EncordClient):
    """
    DEPRECATED - prefer using the :class:`encord.dataset.Dataset` instead
    """

    def get_dataset(self) -> OrmDataset:
        """
        Retrieve dataset info (pointers to data, labels).

        Args:
            self: Encord client object.

        Returns:
            OrmDataset: A dataset record instance.

        Raises:
            AuthorisationError: If the dataset API key is invalid.
            ResourceNotFoundError: If no dataset exists by the specified dataset EntityId.
            UnknownError: If an error occurs while retrieving the dataset.
        """
        return self._querier.basic_getter(OrmDataset)

    def upload_video(self, file_path: str, cloud_upload_settings: CloudUploadSettings = CloudUploadSettings()):
        """
        This function is documented in :meth:`encord.dataset.Dataset.upload_video`.
        """
        if os.path.exists(file_path):
            signed_urls = upload_to_signed_url_list(
                [file_path], self._querier, Video, cloud_upload_settings=cloud_upload_settings
            )
            print("starting upload")
            res = upload_video_to_encord(signed_urls[0], self._querier)
            print("done with upload")
            if res:
                logger.info("Upload complete.")
                return res
            else:
                raise encord.exceptions.EncordException(message="An error has occurred during video upload.")
        else:
            raise encord.exceptions.EncordException(message="{} does not point to a file.".format(file_path))

    def create_image_group(
        self,
        file_paths: typing.Iterable[str],
        max_workers: Optional[int] = None,
        cloud_upload_settings: CloudUploadSettings = CloudUploadSettings(),
    ):
        """
        This function is documented in :meth:`encord.dataset.Dataset.create_image_group`.
        """
        for file_path in file_paths:
            if not os.path.exists(file_path):
                raise encord.exceptions.EncordException(message="{} does not point to a file.".format(file_path))

        successful_uploads = upload_to_signed_url_list(
            file_paths, self._querier, Images, cloud_upload_settings=cloud_upload_settings
        )
        if not successful_uploads:
            raise encord.exceptions.EncordException("All image uploads failed. Image group was not created.")
        upload_images_to_encord(successful_uploads, self._querier)

        image_hash_list = [successful_upload.get("data_hash") for successful_upload in successful_uploads]
        res = self._querier.basic_setter(ImageGroup, uid=image_hash_list, payload={})

        if res:
            titles = [video_data.get("title") for video_data in res]
            logger.info("Upload successful! {} created.".format(titles))
            return res
        else:
            raise encord.exceptions.EncordException(message="An error has occurred during image group creation.")

    def delete_image_group(self, data_hash: str):
        """
        This function is documented in :meth:`encord.dataset.Dataset.delete_image_group`.
        """
        self._querier.basic_delete(ImageGroup, uid=data_hash)

    def delete_data(self, data_hashes: List[str]):
        """
        This function is documented in :meth:`encord.dataset.Dataset.delete_data`.
        """
        self._querier.basic_delete(Video, uid=data_hashes)

    def add_private_data_to_dataset(
        self,
        integration_id: str,
        private_files: Union[str, typing.Dict, Path, typing.TextIO],
        ignore_errors: bool = False,
    ) -> AddPrivateDataResponse:
        """
        This function is documented in :meth:`encord.dataset.Dataset.AddPrivateDataResponse`.
        """
        if isinstance(private_files, dict):
            files = private_files
        elif isinstance(private_files, str):
            if os.path.exists(private_files):
                text_contents = Path(private_files).read_text()
            else:
                text_contents = private_files

            files = json.loads(text_contents)
        elif isinstance(private_files, Path):
            text_contents = private_files.read_text()
            files = json.loads(text_contents)
        elif isinstance(private_files, typing.TextIO):
            text_contents = private_files.read()
            files = json.loads(text_contents)
        else:
            raise ValueError(f"Type [{type(private_files)}] of argument private_files is not supported")

        payload = {"files": files, "integration_id": integration_id, "ignore_errors": ignore_errors}
        response = self._querier.basic_setter(DatasetData, self._config.resource_id, payload=payload)

        return AddPrivateDataResponse.from_dict(response)

    def update_data_item(self, data_hash: str, new_title: str) -> bool:
        """This function is documented in :meth:`encord.dataset.Dataset.update_data_item`."""
        payload = [{"video_hash": data_hash, "title": new_title}]

        response = self._querier.basic_setter(Video, self.get_dataset().dataset_hash, payload=payload)
        try:
            return response.get("success", False)
        except AttributeError:
            return False

    def re_encode_data(self, data_hashes: List[str]):
        """
        This function is documented in :meth:`encord.dataset.Dataset.re_encode_data`.
        """
        payload = {"data_hash": data_hashes}
        return self._querier.basic_put(ReEncodeVideoTask, uid=None, payload=payload)

    def re_encode_data_status(self, job_id: int):
        """
        This function is documented in :meth:`encord.dataset.Dataset.re_encode_data_status`.
        """
        return self._querier.basic_getter(ReEncodeVideoTask, uid=job_id)

    def run_ocr(self, image_group_id: str) -> List[ImageGroupOCR]:
        """
        This function is documented in :meth:`encord.dataset.Dataset.run_ocr`.
        """

        payload = {"image_group_data_hash": image_group_id}

        response = self._querier.get_multiple(ImageGroupOCR, payload=payload)

        return response


CordClientDataset = EncordClientDataset


class EncordClientProject(EncordClient):
    """
    DEPRECATED - prefer using the :class:`encord.project.Project` instead
    """

    def get_project(self):
        """
        Retrieve project info (pointers to data, labels).

        Args:
            self: Encord client object.

        Returns:
            OrmProject: A project record instance.

        Raises:
            AuthorisationError: If the project API key is invalid.
            ResourceNotFoundError: If no project exists by the specified project EntityId.
            UnknownError: If an error occurs while retrieving the project.
        """
        return self._querier.basic_getter(OrmProject)

    def list_label_rows(
        self,
        edited_before: Optional[Union[str, datetime]] = None,
        edited_after: Optional[Union[str, datetime]] = None,
        label_statuses: Optional[List[AnnotationTaskStatus]] = None,
    ) -> List[LabelRowMetadata]:
        if label_statuses:
            label_statuses = [label_status.value for label_status in label_statuses]
        edited_before = parse_datetime("edited_before", edited_before)
        edited_after = parse_datetime("edited_after", edited_after)

        payload = {
            "edited_before": edited_before,
            "edited_after": edited_after,
            "label_statuses": label_statuses,
        }
        return self._querier.get_multiple(LabelRowMetadata, payload=payload)

    def set_label_status(self, label_hash: str, label_status: LabelStatus) -> bool:
        """
        This function is documented in :meth:`encord.project.Project.set_label_status`.
        """
        payload = {
            "label_status": label_status.value,
        }
        return self._querier.basic_setter(LabelStatus, label_hash, payload)

    def add_users(self, user_emails: List[str], user_role: ProjectUserRole) -> List[ProjectUser]:
        """
        This function is documented in :meth:`encord.project.Project.add_users`.
        """

        payload = {"user_emails": user_emails, "user_role": user_role}

        users = self._querier.basic_setter(ProjectUsers, self._config.resource_id, payload=payload)

        return list(map(lambda user: ProjectUser.from_dict(user), users))

    def copy_project(self, copy_datasets=False, copy_collaborators=False, copy_models=False) -> str:
        """
        This function is documented in :meth:`encord.project.Project.copy_project`.
        """

        payload = {"copy_project_options": []}
        if copy_datasets:
            payload["copy_project_options"].append(ProjectCopyOptions.DATASETS.value)
        if copy_models:
            payload["copy_project_options"].append(ProjectCopyOptions.MODELS.value)
        if copy_collaborators:
            payload["copy_project_options"].append(ProjectCopyOptions.COLLABORATORS.value)

        return self._querier.basic_setter(ProjectCopy, self._config.resource_id, payload=payload)

    def get_label_row(self, uid: str, get_signed_url: bool = True):
        """
        This function is documented in :meth:`encord.project.Project.get_label_row`.
        """
        payload = {"get_signed_url": get_signed_url}

        return self._querier.basic_getter(LabelRow, uid, payload=payload)

    def save_label_row(self, uid, label):
        """
        This function is documented in :meth:`encord.project.Project.save_label_row`.
        """
        label = LabelRow(label)
        return self._querier.basic_setter(LabelRow, uid, payload=label)

    def create_label_row(self, uid):
        """
        This function is documented in :meth:`encord.project.Project.create_label_row`.
        """
        return self._querier.basic_put(LabelRow, uid=uid, payload=None)

    def submit_label_row_for_review(self, uid):
        """
        This function is documented in :meth:`encord.project.Project.submit_label_row_for_review`.
        """
        return self._querier.basic_put(Review, uid=uid, payload=None)

    def add_datasets(self, dataset_hashes: List[str]) -> bool:
        """
        This function is documented in :meth:`encord.project.Project.add_datasets`.
        """
        payload = {"dataset_hashes": dataset_hashes}
        return self._querier.basic_setter(ProjectDataset, uid=None, payload=payload)

    def remove_datasets(self, dataset_hashes: List[str]) -> bool:
        """
        This function is documented in :meth:`encord.project.Project.remove_datasets`.
        """
        return self._querier.basic_delete(ProjectDataset, uid=dataset_hashes)

    def get_project_ontology(self) -> Ontology:
        project = self.get_project()
        ontology = project["editor_ontology"]
        return Ontology.from_dict(ontology)

    def add_object(self, name: str, shape: ObjectShape) -> bool:
        """
        This function is documented in :meth:`encord.project.Project.add_object`.
        """
        if len(name) == 0:
            raise ValueError("Ontology object name is empty")

        ontology = self.get_project_ontology()
        ontology.add_object(name, shape)
        return self.__set_project_ontology(ontology)

    def add_classification(
        self,
        name: str,
        classification_type: ClassificationType,
        required: bool,
        options: Optional[typing.Iterable[str]] = None,
    ):
        """
        This function is documented in :meth:`encord.project.Project.add_classification`.
        """
        if len(name) == 0:
            raise ValueError("Ontology classification name is empty")

        ontology = self.get_project_ontology()
        ontology.add_classification(name, classification_type, required, options)
        return self.__set_project_ontology(ontology)

    def create_model_row(
        self,
        title: str,
        description: str,
        features: List[str],
        model: Union[AutomationModels, str],
    ) -> str:
        """
        This function is documented in :meth:`encord.project.Project.create_model_row`.
        """
        if title is None:
            raise encord.exceptions.EncordException(message="You must set a title to create a model row.")

        if features is None:
            raise encord.exceptions.EncordException(
                message="You must pass a list of feature uid's (hashes) to create a model row."
            )

        if isinstance(model, AutomationModels):
            model = model.value

        elif model is None or not AutomationModels.has_value(model):  # Backward compatibility with string options
            raise encord.exceptions.EncordException(
                message="You must pass a model from the `encord.constants.model.AutomationModels` Enum to create a "
                "model row."
            )

        model_row = ModelRow(
            {
                "title": title,
                "description": description,
                "features": features,
                "model": model,
            }
        )

        model = Model(
            {
                "model_operation": ModelOperations.CREATE.value,
                "model_parameters": model_row,
            }
        )

        return self._querier.basic_put(Model, None, payload=model)

    def model_delete(self, uid: str) -> bool:
        """
        This function is documented in :meth:`encord.project.Project.model_delete`.
        """

        return self._querier.basic_delete(Model, uid=uid)

    def model_inference(
        self,
        uid,
        file_paths=None,
        base64_strings=None,
        conf_thresh=0.6,
        iou_thresh=0.3,
        device="cuda",
        detection_frame_range=None,
        allocation_enabled=False,
        data_hashes=None,
        rdp_thresh=0.005,
    ):
        """
        This function is documented in :meth:`encord.project.Project.model_inference`.
        """
        if (file_paths is None and base64_strings is None and data_hashes is None) or (
            file_paths is not None
            and len(file_paths) > 0
            and base64_strings is not None
            and len(base64_strings) > 0
            and data_hashes is not None
            and len(data_hashes) > 0
        ):
            raise encord.exceptions.EncordException(
                message="To run model inference, you must pass either a list of files or base64 strings or list of"
                " data hash."
            )

        if detection_frame_range is None:
            detection_frame_range = []

        files = []
        if file_paths is not None:
            for file_path in file_paths:
                file = open(file_path, "rb").read()
                files.append(
                    {
                        "uid": file_path,  # Add file path as inference identifier
                        "base64_str": base64.b64encode(file).decode("utf-8"),  # File to base64 string
                    }
                )

        elif base64_strings is not None:
            for base64_string in base64_strings:
                files.append(
                    {
                        "uid": str(uuid.uuid4()),  # Add uuid as inference identifier
                        "base64_str": base64_string.decode("utf-8"),  # base64 string to utf-8
                    }
                )

        inference_params = ModelInferenceParams(
            {
                "files": files,
                "conf_thresh": conf_thresh,
                "iou_thresh": iou_thresh,
                "device": device,
                "detection_frame_range": detection_frame_range,
                "allocation_enabled": allocation_enabled,
                "data_hashes": data_hashes,
                "rdp_thresh": rdp_thresh,
            }
        )

        model = Model(
            {
                "model_operation": ModelOperations.INFERENCE.value,
                "model_parameters": inference_params,
            }
        )

        return self._querier.basic_setter(Model, uid, payload=model)

    def model_train(self, uid, label_rows=None, epochs=None, batch_size=24, weights=None, device="cuda"):
        """
        This function is documented in :meth:`encord.project.Project.model_train`.
        """
        if label_rows is None:
            raise encord.exceptions.EncordException(
                message="You must pass a list of label row uid's (hashes) to train a model."
            )

        if epochs is None:
            raise encord.exceptions.EncordException(message="You must set number of epochs to train a model.")

        if batch_size is None:
            raise encord.exceptions.EncordException(message="You must set a batch size to train a model.")

        if weights is None:
            raise encord.exceptions.EncordException(message="You must select model weights to train a model.")

        if device is None:
            raise encord.exceptions.EncordException(message="You must set a device (cuda or CPU) train a model.")

        training_params = ModelTrainingParams(
            {
                "label_rows": label_rows,
                "epochs": epochs,
                "batch_size": batch_size,
                "weights": weights,
                "device": device,
            }
        )

        model = Model(
            {
                "model_operation": ModelOperations.TRAIN.value,
                "model_parameters": training_params,
            }
        )

        return self._querier.basic_setter(Model, uid, payload=model)

    def object_interpolation(
        self,
        key_frames,
        objects_to_interpolate,
    ):
        """
        This function is documented in :meth:`encord.project.Project.object_interpolation`.
        """
        if len(key_frames) == 0 or len(objects_to_interpolate) == 0:
            raise encord.exceptions.EncordException(
                message="To run object interpolation, you must pass key frames and objects to interpolate.."
            )

        interpolation_params = ObjectInterpolationParams(
            {
                "key_frames": key_frames,
                "objects_to_interpolate": objects_to_interpolate,
            }
        )

        algo = LabelingAlgorithm(
            {
                "algorithm_name": INTERPOLATION,
                "algorithm_parameters": interpolation_params,
            }
        )

        return self._querier.basic_setter(LabelingAlgorithm, str(uuid.uuid4()), payload=algo)

    def fitted_bounding_boxes(
        self,
        frames: dict,
        video: dict,
    ):
        """
        This function is documented in :meth:`encord.project.Project.fitted_bounding_boxes`.
        """
        if len(frames) == 0 or len(video) == 0:
            raise encord.exceptions.EncordException(
                message="To run fitting, you must pass frames and video to run bounding box fitting on.."
            )

        fitting_params = BoundingBoxFittingParams(
            {
                "labels": frames,
                "video": video,
            }
        )

        algo = LabelingAlgorithm(
            {
                "algorithm_name": FITTED_BOUNDING_BOX,
                "algorithm_parameters": fitting_params,
            }
        )

        return self._querier.basic_setter(LabelingAlgorithm, str(uuid.uuid4()), payload=algo)

    def get_data(self, data_hash: str, get_signed_url: bool = False) -> Tuple[Optional[Video], Optional[List[Image]]]:
        """
        This function is documented in :meth:`encord.project.Project.get_data`.
        """
        uid = {"data_hash": data_hash, "get_signed_url": get_signed_url}

        dataset_data: DatasetData = self._querier.basic_getter(DatasetData, uid=uid)

        video: Union[Video, None] = None
        if dataset_data["video"] is not None:
            video = Video(dataset_data["video"])

        images: Union[List[Image], None] = None
        if dataset_data["images"] is not None:
            images = []

            for image in dataset_data["images"]:
                images.append(Image(image))

        return video, images

    def get_websocket_url(self) -> str:
        return self._config.get_websocket_url()

    def get_label_logs(
        self, user_hash: str = None, data_hash: str = None, from_unix_seconds: int = None, to_unix_seconds: int = None
    ) -> List[LabelLog]:

        function_arguments = locals()

        query_payload = {k: v for (k, v) in function_arguments.items() if k is not "self" and v is not None}

        return self._querier.get_multiple(LabelLog, payload=query_payload)

    def __set_project_ontology(self, ontology: Ontology) -> bool:
        """
        Save updated project ontology
        Args:
            ontology: the updated project ontology

        Returns:
            bool
        """
        payload = {"editor": ontology.to_dict()}
        return self._querier.basic_setter(OrmProject, uid=None, payload=payload)


CordClientProject = EncordClientProject
