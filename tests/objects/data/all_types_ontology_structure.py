from encord.objects.classification import Classification
from encord.objects.common import (
    ChecklistAttribute,
    FlatOption,
    NestableOption,
    RadioAttribute,
    Shape,
    TextAttribute,
)
from encord.objects.ontology_object import Object
from encord.objects.ontology_structure import OntologyStructure

all_types_structure = OntologyStructure(
    objects=[
        Object(
            uid=1, name="Box", color="#D33115", shape=Shape.BOUNDING_BOX, feature_node_hash="MjI2NzEy", attributes=[]
        ),
        Object(
            uid=2, name="Polygon", color="#E27300", shape=Shape.POLYGON, feature_node_hash="ODkxMzAx", attributes=[]
        ),
        Object(
            uid=3, name="Polyline", color="#16406C", shape=Shape.POLYLINE, feature_node_hash="OTcxMzIy", attributes=[]
        ),
        Object(
            uid=4,
            name="Keypoint Dynamic Answers",
            color="#FE9200",
            shape=Shape.POINT,
            feature_node_hash="MTY2MTQx",
            attributes=[
                TextAttribute(
                    uid=[5, 1], feature_node_hash="OTkxMjU1", name="First name", required=False, dynamic=True
                ),
                ChecklistAttribute(
                    uid=[5, 2],
                    feature_node_hash="ODcxMDAy",
                    name="Mood",
                    required=False,
                    dynamic=True,
                    options=[
                        FlatOption(uid=[5, 2, 1], feature_node_hash="MTE5MjQ3", label="Angry", value="angry"),
                        FlatOption(uid=[5, 2, 2], feature_node_hash="Nzg3MDE3", label="Sad", value="sad"),
                    ],
                ),
            ],
        ),
        Object(
            uid=5,
            name="Nested Box",
            color="#FCDC00",
            shape=Shape.BOUNDING_BOX,
            feature_node_hash="MTA2MjAx",
            attributes=[
                TextAttribute(
                    uid=[5, 1], feature_node_hash="OTkxMjU1", name="First name", required=False, dynamic=False
                ),
                ChecklistAttribute(
                    uid=[5, 2],
                    feature_node_hash="ODcxMDAy",
                    name="Mood",
                    required=False,
                    dynamic=False,
                    options=[
                        FlatOption(uid=[5, 2, 1], feature_node_hash="MTE5MjQ3", label="Angry", value="angry"),
                        FlatOption(uid=[5, 2, 2], feature_node_hash="Nzg3MDE3", label="Sad", value="sad"),
                    ],
                ),
            ],
        ),
        Object(
            uid=6,
            name="Deeply Nested Polygon",
            color="#DBDF00",
            shape=Shape.POLYGON,
            feature_node_hash="MTM1MTQy",
            attributes=[
                RadioAttribute(
                    uid=[6, 1],
                    feature_node_hash="MTExMjI3",
                    name="Radio level 1 ",
                    required=False,
                    dynamic=False,
                    options=[
                        NestableOption(
                            uid=[6, 1, 1],
                            feature_node_hash="MTExNDQ5",
                            label="1 option 1",
                            value="1_option_1",
                            nested_options=[
                                TextAttribute(
                                    uid=[6, 1, 1, 1],
                                    feature_node_hash="MjE2OTE0",
                                    name="1 1 text",
                                    required=False,
                                    dynamic=False,
                                )
                            ],
                        ),
                        NestableOption(
                            uid=[6, 1, 2],
                            feature_node_hash="MTcxMjAy",
                            label="1 option 2",
                            value="1_option_2",
                            nested_options=[
                                RadioAttribute(
                                    uid=[6, 1, 2, 1],
                                    feature_node_hash="NDYyMjQx",
                                    name="1 2 radio 1",
                                    required=False,
                                    dynamic=False,
                                    options=[
                                        NestableOption(
                                            uid=[6, 1, 2, 1, 1],
                                            feature_node_hash="MTY0MzU2",
                                            label="1 2 1 option 1",
                                            value="1_2_1_option_1",
                                            nested_options=[],
                                        ),
                                        NestableOption(
                                            uid=[6, 1, 2, 1, 2],
                                            feature_node_hash="MTI4MjQy",
                                            label="1 2 1 option ",
                                            value="1_2_1_option_",
                                            nested_options=[],
                                        ),
                                    ],
                                )
                            ],
                        ),
                    ],
                )
            ],
        ),
        Object(
            uid=7,
            name="cone object",
            color="#A4DD00",
            shape=Shape.SKELETON,
            feature_node_hash="MTczNjQx",
            attributes=[],
        ),
    ],
    classifications=[
        Classification(
            uid=1,
            feature_node_hash="NzIxNTU1",
            attributes=[
                RadioAttribute(
                    uid=[1, 1],
                    feature_node_hash="MjI5MTA5",
                    name="Radio classification 1",
                    required=False,
                    dynamic=False,
                    options=[
                        NestableOption(
                            uid=[1, 1, 1],
                            feature_node_hash="MTcwMjM5",
                            label="cl 1 option 1",
                            value="cl_1_option_1",
                            nested_options=[],
                        ),
                        NestableOption(
                            uid=[1, 1, 2],
                            feature_node_hash="MjUzMTg1",
                            label="cl 1 option 2",
                            value="cl_1_option_2",
                            nested_options=[
                                TextAttribute(
                                    uid=[1, 1, 2, 1],
                                    feature_node_hash="MTg0MjIw",
                                    name="cl 1 2 text",
                                    required=False,
                                    dynamic=False,
                                )
                            ],
                        ),
                    ],
                )
            ],
        ),
        Classification(
            uid=2,
            feature_node_hash="jPOcEsbw",
            attributes=[
                TextAttribute(
                    uid=[2, 1],
                    feature_node_hash="OxrtEM+v",
                    name="Text classification",
                    required=False,
                    dynamic=False,
                )
            ],
        ),
        Classification(
            uid=3,
            feature_node_hash="3DuQbFxo",
            attributes=[
                ChecklistAttribute(
                    uid=[3, 1],
                    feature_node_hash="9mwWr3OE",
                    name="Checklist classification",
                    required=False,
                    dynamic=False,
                    options=[
                        FlatOption(
                            uid=[3, 1, 1],
                            feature_node_hash="fvLjF0qZ",
                            label="Checklist classification answer 1",
                            value="checklist_classification_answer_1",
                        ),
                        FlatOption(
                            uid=[3, 1, 2],
                            feature_node_hash="a4r7nK9i",
                            label="Checklist classification answer 2",
                            value="checklist_classification_answer_2",
                        ),
                    ],
                )
            ],
        ),
    ],
)
