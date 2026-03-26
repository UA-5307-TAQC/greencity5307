import allure
import pytest
from pytest import fixture
from jsonschema import validate

from schemas.event_comment.event_comment_schema import event_comment_schema

from clients.event_comment_client import EventCommentClient

from data.config import Config

from types import SimpleNamespace


@fixture
def comment_factory(access_token, request):
    """
    Factory fixture to dynamically create comments in tests.
    Guarantees cleanup of all created comments after the test finishes.
    """
    with allure.step("Precondition: The user is logged in."):
        client = EventCommentClient(
            base_url=Config.BASE_API_URL,
            access_token=access_token
        )

    comments_to_delete = []

    def _create_comment(event_id: int, text: str = None) -> int:
        """Inner function, that certain test will call."""
        if text is None:
            text = f"AQA: {request.node.name_schema}"

        with allure.step(f"Step 1: "
                         f"Send a POST request to create a new comment "
                         f"for target event '{event_id}'."):
            response = client.create_comment(event_id=event_id, text=text)
            response_data = response.json()

            if response.status_code == 201:
                comment_id = response_data.get("id")
                if comment_id:
                    comments_to_delete.append(comment_id)
            else:
                pytest.fail(
                    f"Creation failed. Status: {response.status_code}, body: {response.text}"
                )

            validate(instance=response_data, schema=event_comment_schema)

            return comment_id

    yield SimpleNamespace(
        client=client,
        create_comment=_create_comment
    )

    with allure.step("Teardown: Cleaning up all comments created by factory"):
        for c_id in comments_to_delete:
            res = client.delete_comment(comment_id=c_id)
            assert res.status_code in {200, 404}
