"""Schema for Own Security API."""
signin_success_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "required": ["userId", "accessToken", "refreshToken", "name"],
    "properties": {
        "userId": {"type": "integer"},
        "accessToken": {"type": "string"},
        "refreshToken": {"type": "string"},
        "name": {"type": "string"},
        "ownRegistrations": {"type": "boolean"}
    }
}
