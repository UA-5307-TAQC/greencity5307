"""Schema for response data of to-do list item"""

to_do_list_item_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "To-do list item",
    "type": "object",
    "required": ["id", "text"],
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
            "type": ["string", "null"],
            "description": "Status of the task"
        }
    }
}
