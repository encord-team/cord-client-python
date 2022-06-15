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

from collections import OrderedDict
from dataclasses import dataclass
from enum import Enum
from typing import List

from encord.constants.model import AutomationModels
from encord.exceptions import EncordException
from encord.orm import base_orm
from encord.orm.formatter import Formatter
from encord.utilities.common import ENCORD_CONTACT_SUPPORT_EMAIL


class ModelOperations(Enum):
    INFERENCE = 0
    TRAIN = 1
    CREATE = 2


class Model(base_orm.BaseORM):
    """
    Model base ORM.

    ORM:

    model_operation,
    model_parameters,

    """

    DB_FIELDS = OrderedDict([("model_operation", int), ("model_parameters", dict)])


@dataclass
class ModelConfiguration(Formatter):

    model_uid: str
    title: str
    description: str
    # The corresponding feature node hashes of the ontology object
    feature_node_hashes: List[str]
    model: AutomationModels

    @classmethod
    def from_dict(cls, json_dict: dict):
        return ModelConfiguration(
            model_uid=json_dict["model_hash"],
            title=json_dict["title"],
            description=json_dict["description"],
            feature_node_hashes=cls._get_feature_node_hashes(json_dict["features"]),
            model=cls._get_automation_model(json_dict["model"]),
        )

    @classmethod
    def _get_feature_node_hashes(cls, features: dict) -> List[str]:
        return list(features.keys())

    @classmethod
    def _get_automation_model(cls, automation_model_str: str) -> AutomationModels:
        try:
            return AutomationModels(automation_model_str)
        except ValueError as e:
            raise EncordException(
                "A model was returned which was not recognised. Please upgrade your SDK "
                f"to the latest version or contact support at {ENCORD_CONTACT_SUPPORT_EMAIL}."
            ) from e


class ModelRow(base_orm.BaseORM):
    """
    A model row contains a set of features and a model (resnet18, resnet34, resnet50, resnet101, resnet152,
    vgg16, vgg19, yolov5, faster_rcnn, mask_rcnn).

    ORM:

    model_hash (uid),
    title,
    description,
    features,
    model,

    """

    DB_FIELDS = OrderedDict(
        [
            ("model_hash", str),
            ("title", str),
            ("description", str),
            ("features", list),
            ("model", str),
        ]
    )


class ModelInferenceParams(base_orm.BaseORM):
    """
    Model inference parameters for running models trained via the platform.

    ORM:

    local_file_path,
    conf_thresh,
    iou_thresh,
    device
    detection_frame_range (optional)

    """

    DB_FIELDS = OrderedDict(
        [
            ("files", list),
            ("conf_thresh", float),  # Confidence threshold
            ("iou_thresh", float),  # Intersection over union threshold
            ("device", str),
            ("detection_frame_range", list),
            ("allocation_enabled", bool),
            ("data_hashes", list),
            ("rdp_thresh", float),
        ]
    )


class ModelTrainingWeights(base_orm.BaseORM):
    """
    Model training weights.

    ORM:

    training_config_link,
    training_weights_link,

    """

    DB_FIELDS = OrderedDict(
        [
            ("model", str),
            ("training_config_link", str),
            ("training_weights_link", str),
        ]
    )


class ModelTrainingParams(base_orm.BaseORM):
    """
    Model training parameters.

    ORM:

    model_hash,
    label_rows,
    epochs,
    batch_size,
    weights,
    device

    """

    DB_FIELDS = OrderedDict(
        [
            ("model_hash", str),
            ("label_rows", list),
            ("epochs", int),
            ("batch_size", int),
            ("weights", ModelTrainingWeights),
            ("device", str),
        ]
    )
