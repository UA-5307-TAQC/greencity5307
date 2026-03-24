"""Schema for to-do list items response"""

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

# ===================== LIST OF ITEMS =====================

todo_item_schema = {
    "type": "array",
    "minItems": 1,
    "items": todo_item_single_schema
}

# ===================== DELETE (MULTIPLE) =====================

todo_delete_multiple_schema = {
    "type": "integer",
    "minimum": 0
}
