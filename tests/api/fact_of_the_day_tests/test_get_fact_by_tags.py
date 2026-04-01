import allure
from jsonschema import validate

from clients.fact_of_the_day_client import FactOfTheDayClient
from data.config import Config
from schemas.fact_of_the_day_schema import fact_of_the_day_schema


@allure.feature("Fact of the Day")
@allure.story("Get random fact by tags")
@allure.title("Get random fact of the day by tags and validate schema")
def test_get_random_fact_by_tags(access_token):

    client = FactOfTheDayClient(
        base_url=Config.BASE_API_URL,
        access_token=access_token
    )

    user_id = 1205

    response = client.get_random_fact_by_tags(user_id=user_id)

    assert response.status_code == 200

    if response.text == "" or response.text == "null":
        return

    data = response.json()

    validate(instance=data, schema=fact_of_the_day_schema)

    assert "id" in data
    assert isinstance(data["id"], int)
    assert data["id"] > 0

    translations = data["factOfTheDayTranslations"]
    assert isinstance(translations, list)
    assert len(translations) > 0

    language_codes = [t["languageCode"] for t in translations]
    assert "en" in language_codes
    assert "uk" in language_codes
