"""Schema for response data of custom to-do list item"""

custom_to_do_list_item_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Custom to-do list item",
    "type": "object",
    "required": ["id", "text", "status"],
    "properties": {
        "id": {
            "type": "integer",
            "minimum": 1,
            "description": "The unique identifier for item in the habit checklist"
        },
        "text": {
            "type": "string",
            "minLength": 1,
            "description": "The description for item in the habit checklist"
        },
        "status": {
            "type": "string",
            "enum": ["ACTIVE", "DONE", "DISABLED", "INPROGRESS"],
            "description": "Status of the task"
        }
    }
}
