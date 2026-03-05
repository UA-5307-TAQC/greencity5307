"""Create Eco New Schema"""

create_eco_new_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "required": [
        "id",
        "title",
        "content",
        "author",
        "creationDate",
        "imagePath",
        "tagsUk",
        "tagsEn",
        "likes",
        "countComments",
        "countOfEcoNews",
        "favorite"
    ],
    "properties": {
        "id": {
            "type": "integer"
        },
        "title": {
            "type": "string"
        },
        "content": {
            "type": "string"
        },
        "shortInfo": {
            "type": "string"
        },
        "author": {
            "type": "object",
            "required": ["id", "name"],
            "properties": {
                "id": {
                    "type": "integer"
                },
                "name": {
                    "type": "string"
                }
            }
        },
        "creationDate": {
            "type": "string",
            "format": "date-time"
        },
        "imagePath": {
            "type": "string"
        },
        "source": {
            "type": "string"
        },
        "tagsUk": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "tagsEn": {
            "type": "array",
            "items": {
                "type": "string"
            }
        },
        "likes": {
            "type": "integer"
        },
        "countComments": {
            "type": "integer"
        },
        "countOfEcoNews": {
            "type": "integer"
        },
        "favorite": {
            "type": "boolean"
        }
    },
    "additionalProperties": True
}
