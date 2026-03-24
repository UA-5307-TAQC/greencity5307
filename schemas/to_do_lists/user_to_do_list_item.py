"""Schema for response data of user to-do list item"""

user_to_do_list_item = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "User to-do list item",
    "type": "object",
    "required": [
        "id",
        "toDoListItemId",
        "status",
        "dateCompleted",
        "content",
        "boolStatus"
    ],
    "properties": {
        "id": {
            "type": "integer",
            "description": "Record ID"
        },
        "toDoListItemId": {
            "type": "integer",
            "description": "Reference to base to-do item"
        },
        "status": {
            "type": "string",
            "enum": ["ACTIVE", "DONE", "DISABLED", "INPROGRESS"],
            "description": "Current status"
        },
        "dateCompleted": {
            "type": "string",
            "format": "date-time",
            "description": "Completion timestamp"
        },
        "content": {
            "type": "string",
            "description": "Custom content or notes"
        },
        "boolStatus": {
            "type": "boolean",
            "description": "Boolean completion flag"
        }
    }
}
