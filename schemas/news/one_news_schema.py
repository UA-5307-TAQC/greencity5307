"""Schema for response data of one eco news item"""
import copy

one_news_base_required = ["id", "title", "content", "author", "creationDate",
                          "imagePath", "tagsUk", "tagsEn", "likes",
                          "countComments"]
one_news_base_properties = {
    "id": {
        "type": "integer",
        "description": "Unique identifier for the news item",
        "minimum": 1
    },
    "title": {
        "type": "string",
        "description": "News title",
        "minLength": 1
    },
    "content": {
        "type": "string",
        "description": "HTML content of the news",
        "minLength": 1
    },
    "shortInfo": {
        "type": ["string", "null"],
        "description": "Short description or preview text (can be null)"
    },
    "author": {
        "type": "object",
        "description": "Author information",
        "required": ["id", "name"],
        "properties": {
            "id": {
                "type": "integer",
                "description": "Author's unique identifier",
                "minimum": 1
            },
            "name": {
                "type": "string",
                "description": "Author's name",
                "minLength": 1
            }
        },
        "additionalProperties": False
    },
    "creationDate": {
        "type": "string",
        "description": "Date and time when news was created",
        "format": "date-time"
    },
    "imagePath": {
        "type": ["string", "null"],
        "description": "URL to the main image, if null uses default image",
        "format": "uri"
    },
    "tagsUk": {
        "type": "array",
        "description": "Ukrainian tags",
        "items": {
            "type": "string",
            "minLength": 1
        },
        "uniqueItems": True
    },
    "tagsEn": {
        "type": "array",
        "description": "English tags",
        "items": {
            "type": "string",
            "minLength": 1
        },
        "uniqueItems": True
    },
    "likes": {
        "type": "integer",
        "description": "Number of likes",
        "minimum": 0
    },
    "countComments": {
        "type": "integer",
        "description": "Number of comments",
        "minimum": 0
    },
}
one_news_base_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "required": one_news_base_required,
    "properties": one_news_base_properties,
    "additionalProperties": False
}

# for get one by id
one_news_get_by_id_required = [*one_news_base_required, "dislikes", "hidden"]
one_news_get_by_id_properties = copy.deepcopy(one_news_base_properties)
one_news_get_by_id_properties.update({
    "dislikes": {
        "type": "integer",
        "description": "Number of dislikes",
        "minimum": 0
    },
    "hidden": {
        "type": "boolean",
        "description": "Describes if news is hidden",
    },
})
one_news_get_by_id_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": one_news_get_by_id_properties,
    "required": one_news_get_by_id_required,
    "additionalProperties": False
}

# for pages list in find page request
one_news_required = [*one_news_base_required, "source", "countOfEcoNews", "favorite"]
one_news_properties = copy.deepcopy(one_news_base_properties)
one_news_properties.update({
    "source": {
        "type": ["string", "null"],
        "description": "Original source URL (can be null)",
    },
    "countOfEcoNews": {
        "type": "integer",
        "description": "Total count of eco news",
        "minimum": 0
    },
    "favorite": {
        "type": "boolean",
        "description": "Whether the news is marked as favorite"
    }
})
one_news_schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "required": one_news_required,
    "properties": one_news_properties,
    "additionalProperties": False
}
