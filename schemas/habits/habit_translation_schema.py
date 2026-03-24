"""Schema for response data of localized version of a habit’s content"""

habit_translation_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Localized version of a habit’s content",
    "type": "object",
    "required": ["name", "description", "habitItem", "languageCode"],
    "properties": {
        "name": {
            "type": "string",
            "minLength": 1,
            "description": "The localized title of the habit"
        },
        "description": {
            "type": "string",
            "minLength": 1,
            "description": "A detailed explanation of the habit"
        },
        "habitItem": {
            "type": "string",
            "minLength": 1,
            "description": "A short label for the habit goal"
        },
        "languageCode": {
            "type": "string",
            "minLength": 1
        }
    }
}
