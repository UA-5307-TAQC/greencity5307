"""Schema for Google security JSON validation"""
google_security_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "required": [
        "userId",
        "accessToken",
        "refreshToken",
        "name",
        "ownRegistrations",
    ],
    "properties": {
        "userId": {
            "type": "integer"
        },
        "accessToken": {
            "type": "string"
        },
        "refreshToken" : {
            "type": "string"
        },
        "name" : {
            "type": "string"
        },
        "ownRegistrations" : {
            "type": "boolean"
        },
    }
}
