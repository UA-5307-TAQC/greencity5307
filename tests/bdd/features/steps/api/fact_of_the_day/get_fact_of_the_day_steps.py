"""Steps for Fact of the Day API feature (reusing common steps)"""

from behave import when, then

from clients.fact_of_the_day_client import FactOfTheDayClient
from data.config import Config
from schemas.fact_of_the_day_schema import fact_of_the_day_schema


@when("the user sends a request to get a random fact of the day")
def step_get_random_fact(context):
    """Send request to API"""
    client = FactOfTheDayClient(
        base_url=Config.BASE_API_URL,
        access_token=context.auth_token
    )

    context.response = client.get_random_fact()

    context.schema = fact_of_the_day_schema


@then("the response should contain a valid id")
def step_check_id(context):
    """Check id field"""
    data = context.response.json()

    assert "id" in data
    assert isinstance(data["id"], int)
    assert data["id"] > 0


@then('the response should contain translations in "{lang1}" and "{lang2}"')
def step_check_translations(context, lang1, lang2):
    """Check translations"""
    data = context.response.json()

    translations = data["factOfTheDayTranslations"]

    assert isinstance(translations, list)
    assert len(translations) > 0

    language_codes = [t["languageCode"] for t in translations]

    assert lang1 in language_codes, f"{lang1} not found in {language_codes}"
    assert lang2 in language_codes, f"{lang2} not found in {language_codes}"
