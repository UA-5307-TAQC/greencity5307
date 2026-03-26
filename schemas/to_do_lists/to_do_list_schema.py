"""Schema for to-do list items response"""

todo_create_request_schema = {
    "type": "array",
    "minItems": 1,
    "items": {
        "type": "object",
        "required": ["id"],
        "properties": {
            "id": {
                "type": "integer",
                "minimum": 1
            }
        },
        "additionalProperties": False
    }
}

todo_item_single_schema = {
    "type": "object",
    "required": ["id", "text", "status"],
    "properties": {
        "id": {
            "type": "integer",
            "minimum": 1
        },
        "text": {
            "type": "string",
            "minLength": 1
        },
        "status": {
            "type": "string",
            "enum": ["ACTIVE", "DONE", "INPROGRESS"]
        }
    },
    "additionalProperties": False
}


todo_item_schema = {
    "type": "array",
    "minItems": 1,
    "items": todo_item_single_schema
}


todo_delete_multiple_schema = {
    "type": "integer",
    "minimum": 0
}
