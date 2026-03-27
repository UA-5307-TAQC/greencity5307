"""User common schema properties"""

name_schema = {
    "name": {
        "type": "string",
        "pattern": r"^(?!.*\.\.)(?!.*\.$)(?!.*\-\-)(?=[ЄІЇҐЁєіїґёА-Яа-яA-Za-z])"
                   r"[ЄІЇҐЁєіїґёА-Яа-яA-Za-z0-9\s\-'\"’.ʼ]{1,30}(?<![ЭэЁёъЪЫы])$"
    }
}
