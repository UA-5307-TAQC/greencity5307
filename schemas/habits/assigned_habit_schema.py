"""Schema for habit assignment response."""

assigned_habit_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "required": [
        "id",
        "status",
        "createDateTime",
        "habitId",
        "userId",
        "duration",
        "workingDays",
        "habitStreak",
        "lastEnrollment"
    ],
     "properties": {
         "id": {
             "type": "integer",
             "description": "Unique identifier for the assigned habit."
         },
         "status": {
             "type": "string",
             "enum": ["INPROGRESS", "ACQUIRED", "CANCELLED", "EXPIRED", "REQUESTED"],
             "description": "Current state of the assigned habit."
         },
         "createDateTime": {
             "type": "string",
             "description": "The timestamp when the habit was first assigned."
         },
         "habitId": {
             "type": "integer",
             "description": "Reference ID to the specific Habit entity."
         },
         "userId": {
             "type": "integer",
             "description": "Reference ID to the User who owns the assignment."
         },
         "duration": {
             "type": "integer",
             "minimum": 7,
             "maximum": 56,
             "description": "The total length of the habit challenge in days."
         },
         "workingDays": {
             "type": "integer",
             "minimum": 0,
             "description": "The number of days the user has actively engaged with the habit."
         },
         "habitStreak" : {
             "type": "integer",
             "minimum": 0,
             "description": "The current number of consecutive days the habit has been completed."
         },
         "lastEnrollment": {
             "type": "string",
             "description": "The most recent timestamp of habit activity."
         },
         "progressNotificationHasDisplayed": {
             "type": "boolean",
             "default": False,
             "description": "Flag to track if the user has seen the latest progress update."
         }
     }
}
