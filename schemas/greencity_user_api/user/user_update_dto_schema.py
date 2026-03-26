"""User update dto schema"""
from schemas.greencity_user_api.user.common import name_schema

user_update_dto_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        **name_schema,
        "emailNotification": {
            "type": "string",
            "enum": [
                "DISABLED",
                "IMMEDIATELY",
                "DAILY",
                "WEEKLY",
                "MONTHLY"
            ]
        }
    },
    "required": ["emailNotification"],
    "additionalProperties": False
}
