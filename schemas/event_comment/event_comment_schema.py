"""Schema for comment response in EventComment."""

event_comment_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "integer",
            "minimum": 1
        },
        "createdDate": {
            "type": "string",
            "format": "date-time"
        },
        "modifiedDate": {
            "type": "string",
            "format": "date-time"
        },
        "author": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string", "minLength": 1},
                "profilePicturePath": {"type": ["string", "null"]}
            },
            "required": ["id", "name", "profilePicturePath"],
            "additionalProperties": False
        },
        "parentCommentId": {
            "type": ["integer", "null"]
        },
        "text": {
            "type": "string"
        },
        "replies": {
            "type": "integer"
        },
        "likes": {
            "type": "integer"
        },
        "dislikes": {
            "type": "integer"
        },
        "currentUserLiked": {
            "type": "boolean"
        },
        "currentUserDisliked": {
            "type": "boolean"
        },
        "status": {
            "type": "string"
        },
        "additionalImages": {
            "type": "array",
            "items": {"type": "string"}
        }
    },
    "required": [
        "id", "createdDate", "author"
    ],
    "additionalProperties": False
}
