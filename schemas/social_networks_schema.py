"""Social Networks schema"""
social_networks_image_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "required": [
        "id",
        "imagePath",
        "hostPath",
    ],
    "properties": {
        "id": {
            "type": "integer"
        },
        "imagePath": {
            "type":"string"
        },
        "hostPath": {
            "type":"string"
        }
    }
}

social_networks_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "required": [
        "id"
    ],
    "properties": {
        "id": {
            "type": "integer"
        }
    }
}
