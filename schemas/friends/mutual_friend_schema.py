"""Schema for mutual friend response."""

mutual_friend_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "required": ["page", "totalElements", "currentPage", "totalPages"],
    "properties": {
        "page": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["id", "name"],
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"},
                    "email": {"type": "string"},
                    "rating": {"type": "number"},
                    "mutualFriends": {"type": "integer"},
                    "profilePicturePath": {"type": ["string", "null"]},
                    "friendStatus": {"type": "string"},
                    "requesterId": {"type": ["integer", "null"]},
                }
            }
        },
        "totalElements": {"type": "integer"},
        "currentPage": {"type": "integer"},
        "totalPages": {"type": "integer"},
    }
}