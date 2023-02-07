image_group_ontology = {
    "objects": [
        {"id": "1", "name": "Cars", "color": "#D33115", "shape": "bounding_box", "featureNodeHash": "r4M5dkj7"},
        {"id": "2", "name": "Horses", "color": "#E27300", "shape": "bounding_box", "featureNodeHash": "IuyN9D7S"},
        {"id": "3", "name": "Person", "color": "#16406C", "shape": "bounding_box", "featureNodeHash": "vZSR9ig7"},
        {"id": "4", "name": "Bin", "color": "#FE9200", "shape": "bounding_box", "featureNodeHash": "oYAJdhR1"},
        {"id": "5", "name": "Car segmentation", "color": "#FCDC00", "shape": "polygon", "featureNodeHash": "bPAym0bw"},
        {"id": "6", "name": "Bin", "color": "#DBDF00", "shape": "polygon", "featureNodeHash": "cFwx+HfR"},
        {"id": "7", "name": "Camel", "color": "#A4DD00", "shape": "bounding_box", "featureNodeHash": "oyEb2JCi"},
    ],
    "classifications": [
        {
            "id": "1",
            "featureNodeHash": "6nyvIs5W",
            "attributes": [
                {
                    "id": "1.1",
                    "name": "Is there a car in the frame? SUSPECTED",
                    "type": "radio",
                    "required": False,
                    "dynamic": False,
                    "featureNodeHash": "oehdT/Pe",
                    "options": [
                        {"id": "1.1.1", "label": "True", "value": "true", "featureNodeHash": "F/rpk4Fo"},
                        {"id": "1.1.2", "label": "False", "value": "false", "featureNodeHash": "/ILQSY6c"},
                        {"id": "1.1.3", "label": "Maybe", "value": "maybe", "featureNodeHash": "EDWbo8P8"},
                        {"id": "1.1.4", "label": "Maybe not", "value": "maybe_not", "featureNodeHash": "Uxzj/Efq"},
                        {
                            "id": "1.1.5",
                            "label": "SUSPECTED this is not the case",
                            "value": "suspected_this_is_not_the_case",
                            "featureNodeHash": "ZrRZBwx3",
                        },
                    ],
                }
            ],
        },
        {
            "id": "2",
            "featureNodeHash": "R0SMUli5",
            "attributes": [
                {
                    "id": "2.1",
                    "name": "This is a test",
                    "type": "radio",
                    "required": False,
                    "featureNodeHash": "vDUhRPP0",
                    "options": [
                        {"id": "2.1.1", "label": "Test", "value": "test", "featureNodeHash": "P7BwGqM3"},
                        {"id": "2.1.2", "label": "TEst2", "value": "test2", "featureNodeHash": "+LDYFQp1"},
                    ],
                }
            ],
        },
    ],
}


image_group_labels = {
    "label_hash": "f1e6bc82-9f89-4545-8abb-f271bf28cf99",
    "dataset_hash": "d9f19c3c-5cd0-4f8c-b98c-6c0e24676224",
    "dataset_title": "One image group",
    "data_title": "image-group-8375e",
    "data_type": "img_group",
    "data_units": {
        "f850dfb4-7146-49e0-9afc-2b9434a64a9f": {
            "data_hash": "f850dfb4-7146-49e0-9afc-2b9434a64a9f",
            "data_title": "Screenshot 2021-11-24 at 18.35.57.png",
            "data_link": "https://storage.googleapis.com/cord-ai-platform.appspot.com/cord-images-prod/yiA5JxmLEGSoEcJAuxr3AJdDDXE2/f850dfb4-7146-49e0-9afc-2b9434a64a9f?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=firebase-adminsdk-64w1p%40cord-ai-platform.iam.gserviceaccount.com%2F20221206%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20221206T104735Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=969a519552fd513f6401ba72449ea09722ae0c953b5b4c91618f03d345fc96f0e291286e80ef432d13cf70098eb21ef81b0596499f9fd7882706975a1c65987ad7e366d2a0531c917670fff20c5e813e349779518e20c42fdf5b032e9df22f9b72398351cdd76350f24b8a53f900125f87dfb0b0494d164985171181e1dab0cc59a0884daaace3c39d8b7d1f89cb6e57da3db545aacb78d02628eea1e32c0657dbe53a2e697826fc07c28476fcfed9dd24fe1ba842d057a856900f593e06c45bf0ba6e6313d028b1cf142399fc713953984ddfb7403ccdb742268643f99c6183000668f429225a21f4c56cf312f0538951f77494ae6c2698b9190394b0d275bb",
            "data_type": "image/png",
            "data_sequence": "0",
            "width": 952,
            "height": 678,
            "labels": {
                "objects": [
                    {
                        "name": "Cars",
                        "color": "#D33115",
                        "shape": "bounding_box",
                        "value": "cars",
                        "createdAt": "Thu, 01 Dec 2022 13:37:01 GMT",
                        "createdBy": "denis@cord.tech",
                        "confidence": 1,
                        "objectHash": "ApGxvBOz",
                        "featureHash": "r4M5dkj7",
                        "manualAnnotation": True,
                        "boundingBox": {"h": 0.1277, "w": 0.0819, "x": 0.4421, "y": 0.2994},
                        "reviews": [],
                    },
                    {
                        "name": "Car segmentation",
                        "color": "#FCDC00",
                        "shape": "polygon",
                        "value": "car_segmentation",
                        "polygon": {
                            "0": {"x": 0.3183, "y": 0.7655},
                            "1": {"x": 0.307, "y": 0.7559},
                            "2": {"x": 0.2944, "y": 0.7511},
                            "3": {"x": 0.2819, "y": 0.7527},
                            "4": {"x": 0.2716, "y": 0.7607},
                            "5": {"x": 0.2602, "y": 0.7671},
                            "6": {"x": 0.25, "y": 0.7751},
                            "7": {"x": 0.2397, "y": 0.7847},
                            "8": {"x": 0.2306, "y": 0.7959},
                            "9": {"x": 0.2204, "y": 0.8167},
                            "10": {"x": 0.2147, "y": 0.8311},
                            "11": {"x": 0.2101, "y": 0.8503},
                            "12": {"x": 0.2101, "y": 0.8695},
                            "13": {"x": 0.2147, "y": 0.8887},
                            "14": {"x": 0.2181, "y": 0.9047},
                            "15": {"x": 0.2226, "y": 0.9207},
                            "16": {"x": 0.2249, "y": 0.9367},
                            "17": {"x": 0.2306, "y": 0.9527},
                            "18": {"x": 0.2375, "y": 0.9671},
                            "19": {"x": 0.2477, "y": 0.9783},
                            "20": {"x": 0.2591, "y": 0.9847},
                            "21": {"x": 0.2728, "y": 0.9895},
                            "22": {"x": 0.2853, "y": 0.9895},
                            "23": {"x": 0.2967, "y": 0.9911},
                            "24": {"x": 0.3081, "y": 0.9911},
                            "25": {"x": 0.3195, "y": 0.9943},
                            "26": {"x": 0.3309, "y": 0.9927},
                            "27": {"x": 0.3434, "y": 0.9879},
                            "28": {"x": 0.3548, "y": 0.9799},
                            "29": {"x": 0.3651, "y": 0.9703},
                            "30": {"x": 0.3742, "y": 0.9591},
                            "31": {"x": 0.3821, "y": 0.9447},
                            "32": {"x": 0.389, "y": 0.9287},
                            "33": {"x": 0.3935, "y": 0.9095},
                            "34": {"x": 0.3969, "y": 0.8887},
                            "35": {"x": 0.3935, "y": 0.8695},
                            "36": {"x": 0.3878, "y": 0.8551},
                            "37": {"x": 0.381, "y": 0.8407},
                            "38": {"x": 0.3719, "y": 0.8263},
                            "39": {"x": 0.3616, "y": 0.8151},
                            "40": {"x": 0.3525, "y": 0.7991},
                            "41": {"x": 0.3445, "y": 0.7847},
                        },
                        "createdAt": "Tue, 06 Dec 2022 10:46:03 GMT",
                        "createdBy": "denis@cord.tech",
                        "confidence": 1,
                        "objectHash": "85cl/EVa",
                        "featureHash": "bPAym0bw",
                        "lastEditedAt": "Tue, 06 Dec 2022 10:46:05 GMT",
                        "lastEditedBy": "denis@cord.tech",
                        "manualAnnotation": True,
                        "reviews": [],
                    },
                ],
                "classifications": [
                    {
                        "name": "Is there a car in the frame? SUSPECTED",
                        "value": "is_there_a_car_in_the_frame?_suspected",
                        "createdAt": "Tue, 06 Dec 2022 10:45:32 GMT",
                        "createdBy": "denis@cord.tech",
                        "confidence": 1,
                        "featureHash": "6nyvIs5W",
                        "classificationHash": "LzoUFePR",
                        "manualAnnotation": True,
                        "reviews": [],
                    }
                ],
            },
        },
        "177d1bb7-5394-4772-ba9f-4569f0c2a995": {
            "data_hash": "177d1bb7-5394-4772-ba9f-4569f0c2a995",
            "data_title": "Screenshot 2021-11-24 at 18.36.02.png",
            "data_link": "https://storage.googleapis.com/cord-ai-platform.appspot.com/cord-images-prod/yiA5JxmLEGSoEcJAuxr3AJdDDXE2/177d1bb7-5394-4772-ba9f-4569f0c2a995?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=firebase-adminsdk-64w1p%40cord-ai-platform.iam.gserviceaccount.com%2F20221206%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20221206T104735Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=1dc8a21374c868f8966fc1bbf8977cd94dc21995fb126b20fe5339370be4840b79be926686818c77119c90c45079cd64b7f092eae6efddb82d5f76f940f40f03dac19dd7b60b5cd2bafc568a0e9b022c94cc139b327266a319561f113e0de3d49e71c343d2cbae356ae832633e252ca8c4891ab727def04bc93eacce4f86af1ffdb85f0cda9b023fd1675896f0f992d602e452438425be7d985a26a1818def9c6959b585e890a19c7d050d8d94844ff78da520b20be6a8db0c041f48a32148443403ae4917728c2f94e03b2feba96d53797e01fd8714f8493c2d63293654940a83d2b0679c366ddcb6e00157d563a07910962743809455e7a3e7a07f588e4077",
            "data_type": "image/png",
            "data_sequence": "1",
            "width": 952,
            "height": 678,
            "labels": {
                "objects": [
                    {
                        "name": "Cars",
                        "color": "#D33115",
                        "shape": "bounding_box",
                        "value": "cars",
                        "createdAt": "Tue, 06 Dec 2022 10:45:13 GMT",
                        "createdBy": "denis@cord.tech",
                        "isDeleted": False,
                        "confidence": 1,
                        "objectHash": "ApGxvBOz",
                        "featureHash": "r4M5dkj7",
                        "lastEditedAt": "Tue, 06 Dec 2022 10:45:19 GMT",
                        "lastEditedBy": "denis@cord.tech",
                        "manualAnnotation": True,
                        "boundingBox": {"h": 0.1277, "w": 0.0819, "x": 0.4501, "y": 0.2834},
                        "reviews": [],
                    }
                ],
                "classifications": [
                    {
                        "name": "Is there a car in the frame? SUSPECTED",
                        "value": "is_there_a_car_in_the_frame?_suspected",
                        "createdAt": "Tue, 06 Dec 2022 10:45:41 GMT",
                        "createdBy": "denis@cord.tech",
                        "confidence": 1,
                        "featureHash": "6nyvIs5W",
                        "classificationHash": "mBR5wa0v",
                        "manualAnnotation": True,
                        "reviews": [],
                    }
                ],
            },
        },
        "5f393aff-38e3-4364-8ece-340d5aade1c4": {
            "data_hash": "5f393aff-38e3-4364-8ece-340d5aade1c4",
            "data_title": "Screenshot 2021-11-24 at 18.36.07.png",
            "data_link": "https://storage.googleapis.com/cord-ai-platform.appspot.com/cord-images-prod/yiA5JxmLEGSoEcJAuxr3AJdDDXE2/5f393aff-38e3-4364-8ece-340d5aade1c4?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=firebase-adminsdk-64w1p%40cord-ai-platform.iam.gserviceaccount.com%2F20221206%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20221206T104735Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=918e89a6cf98414f475adff1ba4bfafbd615c9432a6229479143434fb2cd00ed62284c331cb047bbe3effa32598a9b522521648e61084a7138eece32c516cd780f982b18398f6557a6c3b9da800cace9244cdf42d39764cdb963745acd6809eb56e02fc81b4119f34f8ad319129a6bac44d87b6e3b7c705635bd3bf7c4c937c811b067469075b816e0a24554ad0b672a0198d0ba4b902e70eb713f38fd6e76f21267d82a00b9db85eb14bb00799bbf9b02f53de26128137a3a04173e00d1caa888249626bee67b012a97f23b14cff68538db5b2b73ea3f4ae31931ac7e05b016defa630a68a4fceb4e07df3ea5d4244e4ba8576d87b1826dc9370d0a4c626b77",
            "data_type": "image/png",
            "data_sequence": "2",
            "width": 952,
            "height": 678,
            "labels": {
                "objects": [
                    {
                        "name": "Cars",
                        "color": "#D33115",
                        "shape": "bounding_box",
                        "value": "cars",
                        "createdAt": "Tue, 06 Dec 2022 10:45:14 GMT",
                        "createdBy": "denis@cord.tech",
                        "isDeleted": False,
                        "confidence": 1,
                        "objectHash": "ApGxvBOz",
                        "featureHash": "r4M5dkj7",
                        "lastEditedAt": "Tue, 06 Dec 2022 10:45:17 GMT",
                        "lastEditedBy": "denis@cord.tech",
                        "manualAnnotation": True,
                        "boundingBox": {"h": 0.1277, "w": 0.0819, "x": 0.4524, "y": 0.3138},
                        "reviews": [],
                    }
                ],
                "classifications": [
                    {
                        "name": "This is a test",
                        "value": "this_is_a_test",
                        "createdAt": "Tue, 06 Dec 2022 10:45:51 GMT",
                        "createdBy": "denis@cord.tech",
                        "confidence": 1,
                        "featureHash": "R0SMUli5",
                        "classificationHash": "TyZQ6kOO",
                        "manualAnnotation": True,
                        "reviews": [],
                    }
                ],
            },
        },
        "6518e742-8dee-4a6d-b491-710f8a5c0fc4": {
            "data_hash": "6518e742-8dee-4a6d-b491-710f8a5c0fc4",
            "data_title": "Screenshot 2021-11-24 at 18.36.11.png",
            "data_link": "https://storage.googleapis.com/cord-ai-platform.appspot.com/cord-images-prod/yiA5JxmLEGSoEcJAuxr3AJdDDXE2/6518e742-8dee-4a6d-b491-710f8a5c0fc4?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=firebase-adminsdk-64w1p%40cord-ai-platform.iam.gserviceaccount.com%2F20221206%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20221206T104735Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=245ddec7e7053e9aa2d826cdf12505973a8d77e1bd28e641d5bdaffafc243d5ec2111225011e3a38f67007c220578858392b92334d706ad4e0c44a7c4c695a0717024ec5aaa73c0f7b0fb805afef221139e92ea39741f0ce69952ce213bffb9362af7df3b1b467ecfc95cdafe8c542612ce8afa49cac159885c8f98be25b6b18c00037dc7cd4c46b9872db100e3935ff2ebdd5751e0bbbad4c86cd9451c190d692872aaa6bef9d34267000b214f78bb7f178343495768556509ce58b565487b9d30e5f8d15b9c56d5765c3cb97dde0e9c0a9cfe4e836ddcbdc07c99b2f94cf56ff516e98ce3cbc54708bbf47d2dba44aee8272c7677fde8feb8323bb8d3ede18",
            "data_type": "image/png",
            "data_sequence": "3",
            "width": 952,
            "height": 678,
            "labels": {
                "objects": [],
                "classifications": [
                    {
                        "name": "This is a test",
                        "value": "this_is_a_test",
                        "createdAt": "Tue, 06 Dec 2022 10:45:51 GMT",
                        "createdBy": "denis@cord.tech",
                        "confidence": 1,
                        "featureHash": "R0SMUli5",
                        "classificationHash": "TyZQ6kOO",
                        "manualAnnotation": True,
                        "reviews": [],
                    }
                ],
            },
        },
        "24dd04ee-ff3f-4f91-b6b5-b385defc7307": {
            "data_hash": "24dd04ee-ff3f-4f91-b6b5-b385defc7307",
            "data_title": "Screenshot 2021-11-24 at 18.36.19.png",
            "data_link": "https://storage.googleapis.com/cord-ai-platform.appspot.com/cord-images-prod/yiA5JxmLEGSoEcJAuxr3AJdDDXE2/24dd04ee-ff3f-4f91-b6b5-b385defc7307?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=firebase-adminsdk-64w1p%40cord-ai-platform.iam.gserviceaccount.com%2F20221206%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20221206T104735Z&X-Goog-Expires=604800&X-Goog-SignedHeaders=host&X-Goog-Signature=43e687ede033723c088a7f5b84ca794b77247e214081d72771e2a3d7928a59ad8a5ec26e6b7ea13a7eb40afcf7f3785bde200706f578bc5bb6c9d94bee996442b658fa32e8da2ef6a32e5695e2ae3624a68b7004e5b5728f3bf03c1be6a6012da922f6e3724256be8601337ce6de3c9e2e2b3ed915049894f831ff1bfabbed83f05701bf5b28628b59fb6a851476567cbb01da8327f95d55934977876b4f376b666fdb0b916dc6c711e6ebaa2cd8c09db12c103e99d02cd84eed102912bf56a21d1480a6dff852a6d7cc24823c8d0cf41e45cbcb136896ea5d120df1eebdf877312e5e6a9347a44dec85e5f00fb3549a289d26afe84666a67f255025f763b032",
            "data_type": "image/png",
            "data_sequence": "4",
            "width": 952,
            "height": 678,
            "labels": {
                "objects": [],
                "classifications": [
                    {
                        "name": "This is a test",
                        "value": "this_is_a_test",
                        "createdAt": "Tue, 06 Dec 2022 10:45:51 GMT",
                        "createdBy": "denis@cord.tech",
                        "confidence": 1,
                        "featureHash": "R0SMUli5",
                        "classificationHash": "TyZQ6kOO",
                        "manualAnnotation": True,
                        "reviews": [],
                    }
                ],
            },
        },
    },
    "object_answers": {
        "ApGxvBOz": {"objectHash": "ApGxvBOz", "classifications": []},
        "85cl/EVa": {"objectHash": "85cl/EVa", "classifications": []},
    },
    "classification_answers": {
        "LzoUFePR": {
            "classificationHash": "LzoUFePR",
            "classifications": [
                {
                    "name": "Is there a car in the frame? SUSPECTED",
                    "value": "is_there_a_car_in_the_frame?_suspected",
                    "answers": [{"name": "True", "value": "true", "featureHash": "F/rpk4Fo"}],
                    "featureHash": "oehdT/Pe",
                    "manualAnnotation": True,
                }
            ],
        },
        "mBR5wa0v": {
            "classificationHash": "mBR5wa0v",
            "classifications": [
                {
                    "name": "Is there a car in the frame? SUSPECTED",
                    "value": "is_there_a_car_in_the_frame?_suspected",
                    "answers": [{"name": "Maybe", "value": "maybe", "featureHash": "EDWbo8P8"}],
                    "featureHash": "oehdT/Pe",
                    "manualAnnotation": True,
                }
            ],
        },
        "TyZQ6kOO": {
            "classificationHash": "TyZQ6kOO",
            "classifications": [
                {
                    "name": "This is a test",
                    "value": "this_is_a_test",
                    "answers": [{"name": "Test", "value": "test", "featureHash": "P7BwGqM3"}],
                    "featureHash": "vDUhRPP0",
                    "manualAnnotation": True,
                }
            ],
        },
    },
    "object_actions": {},
    "label_status": "LABEL_IN_PROGRESS",
}