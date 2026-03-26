"""Schema for response data of habit schema"""

from schemas.habits.habit_translation_schema import habit_translation_schema
from schemas.to_do_lists.to_do_list_item_schema import to_do_list_item_schema
from schemas.to_do_lists.custom_to_do_list_item_schema import custom_to_do_list_item_schema

habit_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "required": [
        "defaultDuration",
        "habitTranslation",
        "id",
        "image",
        "complexity",
        "tags",
        "toDoListItems",
        "likes",
        "dislikes"
    ],
    "properties": {
        "defaultDuration": {
            "type": "integer",
            "description": "Default duration of the habit"
        },
        "amountAcquiredUsers": {
            "type": ["integer", "null"],
            "description": "Number of users who have completed this habit"
        },
        "habitTranslation": habit_translation_schema,
        "id": {
            "type": "integer",
            "description": "Unique identifier of the habit"
        },
        "image": {
            "type": "string",
            "description": "URL or identifier of the habit image"
        },
        "complexity": {
            "type": "integer",
            "minimum": 1,
            "maximum": 3,
            "description": "The difficulty level of the habit: 1 (Low), 2 (Medium), 3 (High)"
        },
        "tags": {
            "type": "array",
            "description": "List of tags associated with the habit",
            "items": {"type": "string"}
        },
        "toDoListItems": {
            "type": "array",
            "items": to_do_list_item_schema,
            "description": "A list of checklist items associated with the habit"
        },
        "customToDoListItems": {
            "type": ["array", "null"],
            "items": custom_to_do_list_item_schema,
            "description": "A list of checklist items associated with the habit"
        },
        "isCustomHabit": {
            "type": ["boolean", "null"],
            "description": "Indicates whether the habit is user-created"
        },
        "usersIdWhoCreatedCustomHabit": {
            "type": ["integer", "null"],
            "description": "User ID who created the custom habit"
        },
        "habitAssignStatus": {
            "anyOf": [
                { "type": "null" },
                {
                    "type": "string",
                    "enum": ["INPROGRESS", "ACQUIRED", "CANCELLED", "EXPIRED", "REQUESTED"]
                }
            ],
            "description": "Assignment status of the habit"
        },
        "isAssigned": {
            "type": ["boolean", "null"],
            "description": "Whether the habit is assigned to the current user"
        },
        "isFavorite": {
            "type": ["boolean", "null"],
            "description": "Whether the habit is marked as favorite"
        },
        "likes": {
            "type": "integer",
            "description": "Number of likes"
        },
        "dislikes": {
            "type": "integer",
            "description": "Number of dislikes"
        }
    }
}
