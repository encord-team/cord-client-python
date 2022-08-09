from encord.objects.common import Shape
from encord.objects.ontology_object import Object
from encord.objects.ontology_structure import OntologyStructure
from encord.transformers.coco.coco_encoder import CocoEncoder
from encord.transformers.coco.coco_transcoders_copied import (
    ConvertFromCordAnnotationFormatToCOCOAnnotationFormat,
)

label_1_image = {
    "label_hash": "21048fb6-fff7-4840-85ed-1a34e5b1ea14",
    "dataset_hash": "aa3c91bd-1363-44a8-9340-12fb15e0e51d",
    "dataset_title": "Dataset multiple image groups",
    "data_title": "labelled-image-group",
    "data_type": "img_group",
    "data_units": {
        "e5e63fe3-6cc6-4e38-baf9-f1fab17c00e7": {
            "data_hash": "e5e63fe3-6cc6-4e38-baf9-f1fab17c00e7",
            "data_title": "apple_158989157.jpeg",
            "data_link": "https://storage.googleapis.com/encord-local-dev.appspot.com/cord-images-dev/lFW59RQ9jcT4vHZeG14m8QWJKug1/e5e63fe3-6cc6-4e38-baf9-f1fab17c00e7?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=firebase-adminsdk-efw44%40encord-local-dev.iam.gserviceaccount.com%2F20220715%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20220715T085658Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=64ab4f3f0b079e238a6a45fa1bca92e62ca23aaf686d89e8e8c1d3afc3fc243997af46dce99aadc2d931e6c759d38f074f7097fd3f4c8f29f6f37b411794ca874b7e6df9b8ee32e70a36a348dca3e308185738ed46dc10c866c394dd643ad8cf414707e30cc3996092a53c34f05b8b7f2300a440ab99c6d907f7380253c3f63196173ec75f8a5b8508b6ba60f3da8cf22bacc46d4edb4802587538af590239c3978612a7ea93d5cbbd7ad9aa5e4d9acfea174cd0fe9154154938cef8d96a1b21d758d2de1e3b91e7b159ad19556c619dc14cef65d457db2aae9080e95fdb1ef5ca316b30eb7eb9c6d8f1043e8b8e8ea7f7f9c95348c093be8cc19a765c74afea",
            "data_type": "image/jpeg",
            "data_sequence": "0",
            "width": 998,
            "height": 1000,
            "labels": {
                "objects": [
                    {
                        "name": "Box - one",
                        "color": "#D33115",
                        "shape": "bounding_box",
                        "value": "box_-_one",
                        "createdAt": "Fri, 15 Jul 2022 08:49:15 GMT",
                        "createdBy": "denis@cord.tech",
                        "confidence": 1,
                        "objectHash": "e54dfcb7",
                        "featureHash": "bce5eafb",
                        "manualAnnotation": True,
                        "boundingBox": {"h": 0.225, "w": 0.3244, "x": 0.5495, "y": 0.0549},
                        "reviews": [],
                    },
                    {
                        "name": "Box - one",
                        "color": "#D33115",
                        "shape": "bounding_box",
                        "value": "box_-_one",
                        "createdAt": "Fri, 15 Jul 2022 08:49:17 GMT",
                        "createdBy": "denis@cord.tech",
                        "confidence": 1,
                        "objectHash": "0e7c3a19",
                        "featureHash": "bce5eafb",
                        "manualAnnotation": True,
                        "boundingBox": {"h": 0.0892, "w": 0.0454, "x": 0.4326, "y": 0.1715},
                        "reviews": [],
                    },
                    {
                        "name": "Polygon",
                        "color": "#E27300",
                        "shape": "polygon",
                        "value": "polygon",
                        "polygon": {
                            "0": {"x": 0.3598, "y": 0.8957},
                            "1": {"x": 0.3818, "y": 0.8971},
                            "2": {"x": 0.3997, "y": 0.8916},
                            "3": {"x": 0.4175, "y": 0.8903},
                            "4": {"x": 0.4395, "y": 0.8916},
                            "5": {"x": 0.4574, "y": 0.8999},
                            "6": {"x": 0.4739, "y": 0.9108},
                            "7": {"x": 0.4945, "y": 0.9122},
                            "8": {"x": 0.5137, "y": 0.9108},
                            "9": {"x": 0.533, "y": 0.9095},
                            "10": {"x": 0.5467, "y": 0.9026},
                            "11": {"x": 0.5646, "y": 0.893},
                            "12": {"x": 0.5825, "y": 0.8848},
                            "13": {"x": 0.6045, "y": 0.8875},
                            "14": {"x": 0.6251, "y": 0.8971},
                            "15": {"x": 0.6416, "y": 0.904},
                            "16": {"x": 0.6622, "y": 0.8971},
                            "17": {"x": 0.6773, "y": 0.8834},
                            "18": {"x": 0.6842, "y": 0.8642},
                            "19": {"x": 0.6801, "y": 0.8505},
                            "20": {"x": 0.6691, "y": 0.8409},
                            "21": {"x": 0.6512, "y": 0.8395},
                            "22": {"x": 0.6251, "y": 0.8422},
                            "23": {"x": 0.6113, "y": 0.8464},
                            "24": {"x": 0.5962, "y": 0.856},
                            "25": {"x": 0.5797, "y": 0.8573},
                            "26": {"x": 0.5605, "y": 0.8546},
                            "27": {"x": 0.544, "y": 0.8532},
                            "28": {"x": 0.5261, "y": 0.8519},
                            "29": {"x": 0.5027, "y": 0.8587},
                            "30": {"x": 0.4918, "y": 0.8711},
                            "31": {"x": 0.478, "y": 0.8697},
                            "32": {"x": 0.4574, "y": 0.8615},
                            "33": {"x": 0.4409, "y": 0.856},
                            "34": {"x": 0.423, "y": 0.856},
                            "35": {"x": 0.4065, "y": 0.856},
                            "36": {"x": 0.3887, "y": 0.856},
                            "37": {"x": 0.3735, "y": 0.8601},
                            "38": {"x": 0.3639, "y": 0.8724},
                        },
                        "createdAt": "Fri, 15 Jul 2022 08:49:39 GMT",
                        "createdBy": "denis@cord.tech",
                        "confidence": 1,
                        "objectHash": "ed7685dc",
                        "featureHash": "aa364ea9",
                        "manualAnnotation": True,
                        "reviews": [],
                    },
                    {
                        "name": "Box - two",
                        "color": "#16406C",
                        "shape": "bounding_box",
                        "value": "box_-_two",
                        "createdAt": "Fri, 15 Jul 2022 08:49:43 GMT",
                        "createdBy": "denis@cord.tech",
                        "confidence": 1,
                        "objectHash": "c3ab2041",
                        "featureHash": "9566d10f",
                        "manualAnnotation": True,
                        "boundingBox": {"h": 0.0837, "w": 0.0811, "x": 0.1124, "y": 0.1687},
                        "reviews": [],
                    },
                    {
                        "name": "Box - two",
                        "color": "#16406C",
                        "shape": "bounding_box",
                        "value": "box_-_two",
                        "createdAt": "Fri, 15 Jul 2022 08:49:44 GMT",
                        "createdBy": "denis@cord.tech",
                        "confidence": 1,
                        "objectHash": "e72c646b",
                        "featureHash": "9566d10f",
                        "manualAnnotation": True,
                        "boundingBox": {"h": 0.0631, "w": 0.0495, "x": 0.1193, "y": 0.2853},
                        "reviews": [],
                    },
                ],
                "classifications": [],
            },
        }
    },
    "object_answers": {
        "e54dfcb7": {"objectHash": "e54dfcb7", "classifications": []},
        "0e7c3a19": {"objectHash": "0e7c3a19", "classifications": []},
        "ed7685dc": {"objectHash": "ed7685dc", "classifications": []},
        "c3ab2041": {"objectHash": "c3ab2041", "classifications": []},
        "e72c646b": {"objectHash": "e72c646b", "classifications": []},
    },
    "classification_answers": {},
    "object_actions": {},
    "label_status": "LABELLED",
}

label_2_images = {
    "label_hash": "776d360c-a2a9-488a-8970-446eb84db817",
    "dataset_hash": "aa3c91bd-1363-44a8-9340-12fb15e0e51d",
    "dataset_title": "Dataset multiple image groups",
    "data_title": "two-ocean-images",
    "data_type": "img_group",
    "data_units": {
        "7913f33d-13bf-4131-9936-0ac56bc61d2f": {
            "data_hash": "7913f33d-13bf-4131-9936-0ac56bc61d2f",
            "data_title": "ocean 2.jpg",
            "data_link": "https://storage.googleapis.com/encord-local-dev.appspot.com/cord-images-dev/lFW59RQ9jcT4vHZeG14m8QWJKug1/7913f33d-13bf-4131-9936-0ac56bc61d2f?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=firebase-adminsdk-efw44%40encord-local-dev.iam.gserviceaccount.com%2F20220715%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20220715T085659Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=9d226856f23e67d1fad5bef61a583eee932f5db1f28c4e10707dc51609cdad8f88bd01873dc345e3d7239297fcc9ddae91424e03efb6fc4eb04d83742c69275da5b79c1ccd38e638034b77f451a97e418c542277c0df7e4a480c900153bcd669bdd29cea9c7f4064b5400ec3d5b31afde036b91231f727e439150284be36b41b59889b5fc442e70584bcb26afc9b8a0810a4cf89d2816c7c6020416515ba3e0064d8b35d776e2edc639be5f4cb1941ac322684e1b6b746357d67eb049b8ac80e5d9f9f30e6cad738c63d7c0ab848923318873f74c75cb7aa1e88692ca585644ecb3cf9b7efbdb596b5dff082829fc15dcab4144ce23fa3fd75b14adb51ab1ec8",
            "data_type": "image/jpg",
            "data_sequence": "0",
            "width": 259,
            "height": 194,
            "labels": {
                "objects": [
                    {
                        "name": "Box - one",
                        "color": "#D33115",
                        "shape": "bounding_box",
                        "value": "box_-_one",
                        "createdAt": "Fri, 15 Jul 2022 08:50:51 GMT",
                        "createdBy": "denis@cord.tech",
                        "confidence": 1,
                        "objectHash": "f2a01cc1",
                        "featureHash": "bce5eafb",
                        "manualAnnotation": True,
                        "boundingBox": {"h": 0.1095, "w": 0.0697, "x": 0.1584, "y": 0.3837},
                        "reviews": [],
                    },
                    {
                        "name": "Box - one",
                        "color": "#D33115",
                        "shape": "bounding_box",
                        "value": "box_-_one",
                        "createdAt": "Fri, 15 Jul 2022 08:50:51 GMT",
                        "createdBy": "denis@cord.tech",
                        "confidence": 1,
                        "objectHash": "907058dd",
                        "featureHash": "bce5eafb",
                        "manualAnnotation": True,
                        "boundingBox": {"h": 0.0825, "w": 0.0382, "x": 0.373, "y": 0.3897},
                        "reviews": [],
                    },
                    {
                        "name": "Box - one",
                        "color": "#D33115",
                        "shape": "bounding_box",
                        "value": "box_-_one",
                        "createdAt": "Fri, 15 Jul 2022 08:50:52 GMT",
                        "createdBy": "denis@cord.tech",
                        "confidence": 1,
                        "objectHash": "4e1d6341",
                        "featureHash": "bce5eafb",
                        "manualAnnotation": True,
                        "boundingBox": {"h": 0.093, "w": 0.0865, "x": 0.4876, "y": 0.3792},
                        "reviews": [],
                    },
                    {
                        "name": "Polygon",
                        "color": "#E27300",
                        "shape": "polygon",
                        "value": "polygon",
                        "polygon": {
                            "0": {"x": 0.4135, "y": 0.6823},
                            "1": {"x": 0.4483, "y": 0.6868},
                            "2": {"x": 0.4775, "y": 0.7048},
                            "3": {"x": 0.4944, "y": 0.7513},
                            "4": {"x": 0.4944, "y": 0.7948},
                            "5": {"x": 0.4775, "y": 0.8158},
                            "6": {"x": 0.4607, "y": 0.8188},
                        },
                        "createdAt": "Fri, 15 Jul 2022 08:50:54 GMT",
                        "createdBy": "denis@cord.tech",
                        "confidence": 1,
                        "objectHash": "d68e323c",
                        "featureHash": "aa364ea9",
                        "manualAnnotation": True,
                        "reviews": [],
                    },
                    {
                        "name": "Box - two",
                        "color": "#16406C",
                        "shape": "bounding_box",
                        "value": "box_-_two",
                        "createdAt": "Fri, 15 Jul 2022 08:50:56 GMT",
                        "createdBy": "denis@cord.tech",
                        "confidence": 1,
                        "objectHash": "31bb5320",
                        "featureHash": "9566d10f",
                        "manualAnnotation": True,
                        "boundingBox": {"h": 0.0855, "w": 0.0596, "x": 0.7966, "y": 0.1302},
                        "reviews": [],
                    },
                ],
                "classifications": [],
            },
        },
        "f2078263-7e8a-4b61-aa7b-1cb00871e381": {
            "data_hash": "f2078263-7e8a-4b61-aa7b-1cb00871e381",
            "data_title": "ocean 1.jpg",
            "data_link": "https://storage.googleapis.com/encord-local-dev.appspot.com/cord-images-dev/lFW59RQ9jcT4vHZeG14m8QWJKug1/f2078263-7e8a-4b61-aa7b-1cb00871e381?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=firebase-adminsdk-efw44%40encord-local-dev.iam.gserviceaccount.com%2F20220715%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20220715T085659Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=03c57dd5bce19592e4684b5fbdb5f2d12c309e3c53b2d426b68c9cd7285ce5d0cde45b244a5f1e16bd27ece847f8570ebd2ce5bca06d48a382e01ba669272ecf2c975b529b61b2daecd7c94eb75568c99b44fdc42f552ddc570f48cf68b453ce688845cba7b76129397e0dec92977f0cde3c994f904de799a057d5df40198812434119e3c4e6b73204feb28a80c56e2f9ff642d990f74f806c193aeec4825d27b4d9bbe7153fd67ee1ee20ee9fb6e2442a3f83e050d209014a8dd82c8bd8c1234496747a94e8994d47782ec1206acd0d40bd3660342d744dd6359fb65bb193167bd119c05d0b6d81245e21f3c77099c185edb158aa29a7e82e1f23178fef3144",
            "data_type": "image/jpg",
            "data_sequence": "1",
            "width": 259,
            "height": 194,
            "labels": {
                "objects": [
                    {
                        "name": "Box - one",
                        "color": "#D33115",
                        "shape": "bounding_box",
                        "value": "box_-_one",
                        "createdAt": "Fri, 15 Jul 2022 08:51:00 GMT",
                        "createdBy": "denis@cord.tech",
                        "confidence": 1,
                        "objectHash": "0afa8bf6",
                        "featureHash": "bce5eafb",
                        "lastEditedAt": "Fri, 15 Jul 2022 08:51:14 GMT",
                        "lastEditedBy": "denis@cord.tech",
                        "manualAnnotation": True,
                        "boundingBox": {"h": 0.2745, "w": 0.1371, "x": 0.6315, "y": 0.0132},
                        "reviews": [],
                    },
                    {
                        "name": "Box - two",
                        "color": "#16406C",
                        "shape": "bounding_box",
                        "value": "box_-_two",
                        "createdAt": "Fri, 15 Jul 2022 08:51:03 GMT",
                        "createdBy": "denis@cord.tech",
                        "confidence": 1,
                        "objectHash": "f104f342",
                        "featureHash": "9566d10f",
                        "manualAnnotation": True,
                        "boundingBox": {"h": 0.3285, "w": 0.0843, "x": 0.4854, "y": 0.3312},
                        "reviews": [],
                    },
                    {
                        "name": "Polygon",
                        "color": "#E27300",
                        "shape": "polygon",
                        "value": "polygon",
                        "polygon": {
                            "0": {"x": 0.3, "y": 0.5818},
                            "1": {"x": 0.3022, "y": 0.5968},
                            "2": {"x": 0.3079, "y": 0.6343},
                            "3": {"x": 0.318, "y": 0.6928},
                            "4": {"x": 0.3247, "y": 0.7168},
                            "5": {"x": 0.3371, "y": 0.7393},
                            "6": {"x": 0.3573, "y": 0.7603},
                            "7": {"x": 0.3708, "y": 0.7693},
                            "8": {"x": 0.382, "y": 0.7783},
                            "9": {"x": 0.3944, "y": 0.7888},
                            "10": {"x": 0.4101, "y": 0.7993},
                            "11": {"x": 0.4348, "y": 0.8128},
                            "12": {"x": 0.4551, "y": 0.8248},
                            "13": {"x": 0.491, "y": 0.8413},
                            "14": {"x": 0.509, "y": 0.8488},
                            "15": {"x": 0.5382, "y": 0.8548},
                            "16": {"x": 0.5742, "y": 0.8563},
                            "17": {"x": 0.6, "y": 0.8503},
                            "18": {"x": 0.6315, "y": 0.8323},
                            "19": {"x": 0.6562, "y": 0.8098},
                            "20": {"x": 0.6674, "y": 0.7888},
                            "21": {"x": 0.6854, "y": 0.7558},
                            "22": {"x": 0.6921, "y": 0.7423},
                            "23": {"x": 0.7034, "y": 0.7168},
                            "24": {"x": 0.7112, "y": 0.6958},
                            "25": {"x": 0.7135, "y": 0.6763},
                            "26": {"x": 0.7135, "y": 0.6523},
                            "27": {"x": 0.7112, "y": 0.6343},
                            "28": {"x": 0.7045, "y": 0.6178},
                            "29": {"x": 0.6955, "y": 0.6043},
                            "30": {"x": 0.6809, "y": 0.6133},
                            "31": {"x": 0.6685, "y": 0.6328},
                            "32": {"x": 0.6539, "y": 0.6673},
                            "33": {"x": 0.6427, "y": 0.6958},
                            "34": {"x": 0.6236, "y": 0.7198},
                            "35": {"x": 0.5989, "y": 0.7393},
                            "36": {"x": 0.582, "y": 0.7483},
                            "37": {"x": 0.564, "y": 0.7543},
                            "38": {"x": 0.5517, "y": 0.7588},
                            "39": {"x": 0.5382, "y": 0.7633},
                            "40": {"x": 0.5225, "y": 0.7663},
                            "41": {"x": 0.5, "y": 0.7708},
                            "42": {"x": 0.4573, "y": 0.7693},
                            "43": {"x": 0.4371, "y": 0.7633},
                            "44": {"x": 0.4236, "y": 0.7528},
                            "45": {"x": 0.4124, "y": 0.7348},
                            "46": {"x": 0.3966, "y": 0.7093},
                            "47": {"x": 0.3876, "y": 0.6883},
                            "48": {"x": 0.3798, "y": 0.6718},
                            "49": {"x": 0.373, "y": 0.6568},
                            "50": {"x": 0.364, "y": 0.6403},
                            "51": {"x": 0.3506, "y": 0.6223},
                            "52": {"x": 0.3404, "y": 0.6088},
                            "53": {"x": 0.3326, "y": 0.5968},
                            "54": {"x": 0.3236, "y": 0.5863},
                        },
                        "createdAt": "Fri, 15 Jul 2022 08:51:09 GMT",
                        "createdBy": "denis@cord.tech",
                        "confidence": 1,
                        "objectHash": "7ce9d27e",
                        "featureHash": "aa364ea9",
                        "manualAnnotation": True,
                        "reviews": [],
                    },
                    {
                        "name": "Box - one",
                        "color": "#D33115",
                        "shape": "bounding_box",
                        "value": "box_-_one",
                        "createdAt": "Fri, 15 Jul 2022 08:51:18 GMT",
                        "createdBy": "denis@cord.tech",
                        "confidence": 1,
                        "objectHash": "827d1547",
                        "featureHash": "bce5eafb",
                        "manualAnnotation": True,
                        "boundingBox": {"h": 0.2925, "w": 0.1472, "x": 0.2798, "y": 0.0027},
                        "reviews": [],
                    },
                ],
                "classifications": [],
            },
        },
    },
    "object_answers": {
        "f2a01cc1": {"objectHash": "f2a01cc1", "classifications": []},
        "907058dd": {"objectHash": "907058dd", "classifications": []},
        "4e1d6341": {"objectHash": "4e1d6341", "classifications": []},
        "d68e323c": {"objectHash": "d68e323c", "classifications": []},
        "31bb5320": {"objectHash": "31bb5320", "classifications": []},
        "0afa8bf6": {"objectHash": "0afa8bf6", "classifications": []},
        "f104f342": {"objectHash": "f104f342", "classifications": []},
        "7ce9d27e": {"objectHash": "7ce9d27e", "classifications": []},
        "827d1547": {"objectHash": "827d1547", "classifications": []},
    },
    "classification_answers": {},
    "object_actions": {},
    "label_status": "LABELLED",
}

ontology = OntologyStructure(
    objects=[
        Object(
            uid=1,
            name="Box - one",
            color="#D33115",
            shape=Shape.BOUNDING_BOX,
            feature_node_hash="bce5eafb",
            attributes=[],
        ),
        Object(
            uid=2,
            name="Polygon",
            color="#E27300",
            shape=Shape.POLYGON,
            feature_node_hash="aa364ea9",
            attributes=[],
        ),
        Object(
            uid=3,
            name="Box - two",
            color="#16406C",
            shape=Shape.BOUNDING_BOX,
            feature_node_hash="9566d10f",
            attributes=[],
        ),
    ],
    classifications=[],
)


def test_coco_encoder_1():
    x = ConvertFromCordAnnotationFormatToCOCOAnnotationFormat(example_label_2)
    print(x)

    # assert x == output_2


def test_coco_encoder_2():
    x = CocoEncoder(label_2_images, ontology).encode()
    print(x)

    output = {
        "info": {
            "description": "two-ocean-images",
            "contributor": None,
            "date_created": None,
            "url": None,
            "version": None,
            "year": None,
        },
        "categories": [
            {"supercategory": "bounding_box", "id_": 0, "name": "Box - one"},
            {"supercategory": "polygon", "id_": 1, "name": "Polygon"},
            {"supercategory": "bounding_box", "id_": 2, "name": "Box - two"},
        ],
        "images": {},
        "annotations": [
            [
                {
                    "area": 0.0152643,
                    "bbox": [0.1584, 0.7674, 0.0697, 0.219],
                    "category_id": 0,
                    "id_": 0,
                    "image_id": 0,
                    "iscrowd": 0,
                    "segmentation": [
                        [
                            0.1584,
                            0.7674,
                            0.22810000000000002,
                            0.7674,
                            0.22810000000000002,
                            0.9863999999999999,
                            0.1584,
                            0.9863999999999999,
                        ]
                    ],
                    "keypoints": None,
                    "num_keypoints": None,
                },
                {
                    "area": 0.006303,
                    "bbox": [0.373, 0.7794, 0.0382, 0.165],
                    "category_id": 0,
                    "id_": 1,
                    "image_id": 0,
                    "iscrowd": 0,
                    "segmentation": [[0.373, 0.7794, 0.4112, 0.7794, 0.4112, 0.9444, 0.373, 0.9444]],
                    "keypoints": None,
                    "num_keypoints": None,
                },
                {
                    "area": 0.016089,
                    "bbox": [0.4876, 0.7584, 0.0865, 0.186],
                    "category_id": 0,
                    "id_": 2,
                    "image_id": 0,
                    "iscrowd": 0,
                    "segmentation": [
                        [
                            0.4876,
                            0.7584,
                            0.5740999999999999,
                            0.7584,
                            0.5740999999999999,
                            0.9443999999999999,
                            0.4876,
                            0.9443999999999999,
                        ]
                    ],
                    "keypoints": None,
                    "num_keypoints": None,
                },
                {
                    "area": 0.012644850000000006,
                    "bbox": [0.4135, 1.3646, 0.08090000000000003, 0.2729999999999999],
                    "category_id": 1,
                    "id_": 3,
                    "image_id": 0,
                    "iscrowd": 0,
                    "segmentation": [
                        [
                            0.4135,
                            1.3646,
                            0.4483,
                            1.3736,
                            0.4775,
                            1.4096,
                            0.4944,
                            1.5026,
                            0.4944,
                            1.5896,
                            0.4775,
                            1.6316,
                            0.4607,
                            1.6376,
                        ]
                    ],
                    "keypoints": None,
                    "num_keypoints": None,
                },
                {
                    "area": 0.0101916,
                    "bbox": [0.7966, 0.2604, 0.0596, 0.171],
                    "category_id": 2,
                    "id_": 4,
                    "image_id": 0,
                    "iscrowd": 0,
                    "segmentation": [[0.7966, 0.2604, 0.8562, 0.2604, 0.8562, 0.4314, 0.7966, 0.4314]],
                    "keypoints": None,
                    "num_keypoints": None,
                },
            ],
            [
                {
                    "area": 0.07526790000000001,
                    "bbox": [0.6315, 0.0264, 0.1371, 0.549],
                    "category_id": 0,
                    "id_": 5,
                    "image_id": 1,
                    "iscrowd": 0,
                    "segmentation": [[0.6315, 0.0264, 0.7686, 0.0264, 0.7686, 0.5754, 0.6315, 0.5754]],
                    "keypoints": None,
                    "num_keypoints": None,
                },
                {
                    "area": 0.0553851,
                    "bbox": [0.4854, 0.6624, 0.0843, 0.657],
                    "category_id": 2,
                    "id_": 6,
                    "image_id": 1,
                    "iscrowd": 0,
                    "segmentation": [[0.4854, 0.6624, 0.5697, 0.6624, 0.5697, 1.3194, 0.4854, 1.3194]],
                    "keypoints": None,
                    "num_keypoints": None,
                },
                {
                    "area": 0.08128949999999996,
                    "bbox": [0.3, 1.1636, 0.41350000000000003, 0.5489999999999999],
                    "category_id": 1,
                    "id_": 7,
                    "image_id": 1,
                    "iscrowd": 0,
                    "segmentation": [
                        [
                            0.3,
                            1.1636,
                            0.3022,
                            1.1936,
                            0.3079,
                            1.2686,
                            0.318,
                            1.3856,
                            0.3247,
                            1.4336,
                            0.3371,
                            1.4786,
                            0.3573,
                            1.5206,
                            0.3708,
                            1.5386,
                            0.382,
                            1.5566,
                            0.3944,
                            1.5776,
                            0.4101,
                            1.5986,
                            0.4348,
                            1.6256,
                            0.4551,
                            1.6496,
                            0.491,
                            1.6826,
                            0.509,
                            1.6976,
                            0.5382,
                            1.7096,
                            0.5742,
                            1.7126,
                            0.6,
                            1.7006,
                            0.6315,
                            1.6646,
                            0.6562,
                            1.6196,
                            0.6674,
                            1.5776,
                            0.6854,
                            1.5116,
                            0.6921,
                            1.4846,
                            0.7034,
                            1.4336,
                            0.7112,
                            1.3916,
                            0.7135,
                            1.3526,
                            0.7135,
                            1.3046,
                            0.7112,
                            1.2686,
                            0.7045,
                            1.2356,
                            0.6955,
                            1.2086,
                            0.6809,
                            1.2266,
                            0.6685,
                            1.2656,
                            0.6539,
                            1.3346,
                            0.6427,
                            1.3916,
                            0.6236,
                            1.4396,
                            0.5989,
                            1.4786,
                            0.582,
                            1.4966,
                            0.564,
                            1.5086,
                            0.5517,
                            1.5176,
                            0.5382,
                            1.5266,
                            0.5225,
                            1.5326,
                            0.5,
                            1.5416,
                            0.4573,
                            1.5386,
                            0.4371,
                            1.5266,
                            0.4236,
                            1.5056,
                            0.4124,
                            1.4696,
                            0.3966,
                            1.4186,
                            0.3876,
                            1.3766,
                            0.3798,
                            1.3436,
                            0.373,
                            1.3136,
                            0.364,
                            1.2806,
                            0.3506,
                            1.2446,
                            0.3404,
                            1.2176,
                            0.3326,
                            1.1936,
                            0.3236,
                            1.1726,
                        ]
                    ],
                    "keypoints": None,
                    "num_keypoints": None,
                },
                {
                    "area": 0.086112,
                    "bbox": [0.2798, 0.0054, 0.1472, 0.585],
                    "category_id": 0,
                    "id_": 8,
                    "image_id": 1,
                    "iscrowd": 0,
                    "segmentation": [
                        [0.2798, 0.0054, 0.427, 0.0054, 0.427, 0.5903999999999999, 0.2798, 0.5903999999999999]
                    ],
                    "keypoints": None,
                    "num_keypoints": None,
                },
            ],
        ],
    }
