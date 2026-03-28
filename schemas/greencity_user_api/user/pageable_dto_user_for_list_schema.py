"""User pages schemas"""

from schemas.greencity_user_api.user.common import name_schema

user_for_list_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "required": ["id", "email", "userStatus", "role"],
    "properties": {
        "id": {
            "type": "integer"
        },
        **name_schema,
        "dateOfRegistration": {
            "type": "string",
            "format": "date-time"
        },
        "email": {
            "type": "string",
            "format": "email"
        },
        "userStatus": {
            "type": "string",
            "enum": ["CREATED", "VERIFIED"]
        },
        "role": {
            "type": "string",
            "enum": [
                "ROLE_USER",
                "ROLE_ADMIN",
                "ROLE_MODERATOR",
                "ROLE_EMPLOYEE",
                "ROLE_UBS_EMPLOYEE"
            ]
        }
    },
    "additionalProperties": False
}

pageable_dto_user_for_list_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "required": ["page", "totalElements", "currentPage", "totalPages"],
    "properties": {
        "page": {
            "type": "array",
            "items": user_for_list_schema,
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
    "additionalProperties": False
}
