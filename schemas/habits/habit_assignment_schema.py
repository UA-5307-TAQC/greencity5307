"""Schema for the current user's habit assign"""

from schemas.habits.habit_schema import habit_schema
from schemas.to_do_lists.user_to_do_list_item import user_to_do_list_item

habit_assignment_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "required": [
        "createDateTime",
        "duration",
        "habit",
        "habitStreak",
        "id",
        "lastEnrollmentDate",
        "status",
        "userId",
        "workingDays"
    ],
    "properties":{
        "createDateTime": {
            "type": "string",
            "format": "date-time",
            "description": "Timestamp when the habit was assigned to the user"
        },
        "duration": {
            "type": "integer",
            "description": "Duration in days or units for the habit"
        },
        "habit": habit_schema,
        "userToDoListItems": {
            "type": ["array", "null"],
            "items": user_to_do_list_item,
            "description": "A list of checklist items associated with the habit"
        },
        "habitStatusCalendarDtoList": {
            "type": "array",
            "description": "Calendar tracking entries for the habit",
            "items": {
                "type": "object",
                "properties": {
                    "enrollDate": {
                        "type": "string",
                        "format": "date",
                        "description": "Date of habit activity"
                    },
                    "id": {
                        "type": "integer",
                        "minimum": 1,
                        "description": "Record ID"
                    }
                },
                "required": ["enrollDate", "id"]
            }
        },
        "habitStreak": {
            "type": "integer",
            "description": "Number of consecutive days the habit was performed"
        },
        "id": {
            "type": "integer",
            "description": "Unique identifier of the habit assignment"
        },
        "lastEnrollmentDate": {
            "type": "string",
            "format": "date-time",
            "description": "Last date when the habit was performed"
        },
        "status": {
            "type": "string",
            "enum": ["INPROGRESS", "ACQUIRED", "CANCELLED", "EXPIRED", "REQUESTED"],
            "description": "Overall habit status for the user"
        },
        "userId": {
            "type": "integer",
            "description": "ID of the user"
        },
        "workingDays": {
            "type": "integer",
            "description": "Number of days the user worked on the habit"
        },
        "progressNotificationHasDisplayed": {
            "type": ["boolean", "null"],
            "description": "Indicates if progress notification was shown"
        },
        "friendsIdsTrackingHabit": {
            "type": "array",
            "description": "List of friend IDs tracking this habit",
            "items": {"type": "integer"}
        }
    }
}
