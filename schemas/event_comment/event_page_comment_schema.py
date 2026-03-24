"""Schema for comments list response in EventComment."""
from schemas.event_comment.event_comment_schema import event_comment_schema


event_comments_list_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "page": {
            "type": "array",
            "items": event_comment_schema
        },
        "totalElements": {
            "type": "integer"
        },
        "currentPage": {
            "type": "integer"
        },
        "totalPages": {
            "type": "integer"
        }
    },
    "required": ["page", "totalElements", "currentPage", "totalPages"],
    "additionalProperties": False
}
