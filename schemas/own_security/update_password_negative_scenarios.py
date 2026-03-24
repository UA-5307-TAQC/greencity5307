""" Negative scenario for updating password """

status_code_400_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "anyOf": [
        {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["name", "message"],
                "properties": {
                    "name": {"type": "string"},
                    "message": {"type": "string"}
                }
            }
        },
        {
            "type": "object",
            "required": ["name", "message"],
            "properties": {
                "name": {"type": "string"},
                "message": {"type": "string"}
            }
        }
    ]
}

status_code_401_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "required": ["timestamp", "status", "error", "path"],
    "properties": {
        "timestamp": {"type": "string"},
        "status": {"type": "integer"},
        "error": {"type": "string"},
        "path": {"type": "string"}
    }
}
