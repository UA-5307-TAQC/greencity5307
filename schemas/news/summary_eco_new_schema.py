"""Summary eco new schema"""
summary_eco_new_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "additionalProperties": False,
    "required": [
        "content"
    ],
    "properties": {
        "content": {
            "type": "string"
        },
        "source": {
            "type": ["string" ,"null"]
        }
    }
}
