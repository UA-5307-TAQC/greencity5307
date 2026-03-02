"""Schema for response data for eco news GET request"""

from utils.Schemas.news.one_news_schema import one_news_schema

eco_news_response_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "totalElements": {
            "type": "integer",
            "description": "Total count of eco news",
            "minimum": 0 # maybe this should be 1
        },
        "currentPage": {
            "type": "integer",
            "description": "Current page number for pagination",
            "minimum": 0
        },
        "totalPages": {
            "type": "integer",
            "description": "Total count of eco news pages",
            "minimum": 0
        },
        "number": {
            "type": "integer",
            "description": "Also shows current page number",
            "minimum": 0
        },
        "first": {
            "type": "boolean",
            "description": "Tell whether this is the first page",
        },
        "last": {
            "type": "boolean",
            "description": "Tell whether this is the last page",
        },
        "hasPrevious": {
            "type": "boolean",
            "description": "Tell whether this page has previous page",
        },
        "hasNext": {
            "type": "boolean",
            "description": "Tell whether this page has next page",
        },
        "page": {
            "type": "array",
            "items": one_news_schema,
            "description": "List of news items on current page"
        }
    }
}
