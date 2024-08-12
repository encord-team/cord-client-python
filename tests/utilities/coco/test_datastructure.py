import json
from pathlib import Path

import numpy as np
import pytest

from encord.utilities.coco.datastructure import (
    CocoAnnotationModel,
    CocoBoundingBox,
    CocoPolygon,
    CocoRLE,
    CocoRootModel,
)

DATA_DIR = Path(__file__).parent / "data"


@pytest.fixture
def coco_sample() -> dict:
    return json.loads((DATA_DIR / "coco_sample.json").read_text())


def get_bbox_from_polygon(polygon: CocoPolygon) -> CocoBoundingBox:
    min_x = min(point.x for point in polygon.values)
    min_y = min(point.y for point in polygon.values)
    max_x = max(point.x for point in polygon.values)
    max_y = max(point.y for point in polygon.values)
    return CocoBoundingBox(x=min_x, y=min_y, w=max_x - min_x, h=max_y - min_y)


def polygon_area(polygon: CocoPolygon) -> float:
    area = 0.0
    for i in range(len(polygon.values)):
        area += polygon.values[i - 1].x * (polygon.values[i].y - polygon.values[i - 2].y)
    return abs(area / 2)


def test_coco_annotation_model_with_missing_segmentation_field(coco_sample: dict) -> None:
    for ann in coco_sample["annotations"]:
        ann.pop("segmentation")
        ann_model = CocoAnnotationModel.from_dict(ann)
        # Assert the generated segmentation is a polygon with 4 points
        assert isinstance(ann_model.segmentation, CocoPolygon) and len(ann_model.segmentation.values) == 4
        # Assert the bounding box containing the generated polygon is the same as the input bounding box
        containing_bbox = get_bbox_from_polygon(ann_model.segmentation)
        assert np.allclose(containing_bbox, ann_model.bbox)
        # Assert the area of the generated polygon is the same as the area of the input bounding box
        assert np.isclose(polygon_area(ann_model.segmentation), ann_model.bbox.w * ann_model.bbox.h)


def test_coco_model_label_validation(coco_sample: dict) -> None:
    # TODO Add annotation samples that correspond to multipolygons
    coco_model = CocoRootModel.from_dict(coco_sample)
    assert sum(isinstance(ann.segmentation, CocoRLE) for ann in coco_model.annotations) == 5
    assert sum(isinstance(ann.segmentation, CocoPolygon) for ann in coco_model.annotations) == 465
    assert sum(isinstance(ann.segmentation, (CocoRLE, CocoPolygon)) for ann in coco_model.annotations) == 5 + 465
