"""Schema for response fact of the day"""

fact_of_the_day_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Fact of the day",
    "type": "object",
    "required": ["id", "factOfTheDayTranslations"],
    "properties": {
        "id": {
            "type": "integer",
            "minimum": 1,
            "description": "The unique identifier of the fact"
        },
        "factOfTheDayTranslations": {
            "type": "array",
            "description": "List of translations of the fact",
            "items": {
                "type": "object",
                "required": ["content", "languageCode"],
                "properties": {
                    "content": {
                        "type": "string",
                        "minLength": 1,
                        "maxLength": 300,
                        "description": "Content of the fact"
                    },
                    "languageCode": {
                        "type": "string",
                        "description": "Language code of the translation (e.g. en, uk)"
                    }
                }
            }
        }
    }
}
