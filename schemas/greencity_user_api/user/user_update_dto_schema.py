"""User update dto schema"""

user_update_dto_schema = {
    "type": "object",
    "properties": {
        "name": {
            "type": "string",
            "pattern": r"^(?!.*\.\.)(?!.*\.$)(?!.*\-\-)(?=[ЄІЇҐЁєіїґёА-Яа-яA-Za-z])"
                       r"[ЄІЇҐЁєіїґёА-Яа-яA-Za-z0-9\s\-'\"’.ʼ]{1,30}(?<![ЭэЁёъЪЫы])$"
        },
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
