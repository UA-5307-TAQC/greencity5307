"""Client for interacting with ToDo list API"""
import allure
from requests import Response

from clients.base_client import BaseClient


class TodoClient(BaseClient):
    """Client for ToDo list endpoints"""

    def __init__(self, base_url, access_token=None):
        super().__init__(
            base_url=base_url,
            access_token=access_token
        )

    @allure.step("Create to-do list items for habitId={habit_id}")
    def create_todo_items(self, habit_id: int, body: list, lang: str = "en") -> Response:
        """Create to-do list items for habitId"""
        return self._request(
            method="POST",
            endpoint="/user/to-do-list-items",
            params={
                "habitId": habit_id,
                "lang": lang
            },
            json=body
        )

#     def __init__(self, base_url, access_token=None):
#         super().__init__(
#             base_url=f"{base_url}/user/to-do-list-items",
#             access_token=access_token
#         )
#
#     # ===================== CREATE =====================
#
#     @allure.step("Create to-do list items for habitId={habit_id}")
#     def create_todo_items(self, habit_id: int, body: list, lang: str = "en") -> Response:
#         """Create to-do list items for habitId"""
#         return self._request(
#             method="POST",
#             endpoint="",
#             params={
#                 "habitId": habit_id,
#                 "lang": lang
#             },
#             json=body
#         )
#
#     # ===================== GET =====================
#
    @allure.step("Get to-do list by habitId={habit_id}")
    def get_todo_list(self, habit_id: int, lang: str = "en") -> Response:
        """Get to-do list by habitId"""
        return self._request(
            method="GET",
            endpoint=f"/habits/{habit_id}/to-do-list",
            params={"lang": lang}
        )

    @allure.step("Get INPROGRESS to-do list for userId={user_id}")
    def get_inprogress_items(self, user_id: int, lang: str = "en") -> Response:
        """Get to-do list by userId"""
        return self._request(
            method="GET",
            endpoint=f"/{user_id}/get-all-inprogress",
            params={"lang": lang}
        )

    # ===================== UPDATE =====================

    @allure.step("Mark to-do item as DONE userToDoListItemId={item_id}")
    def mark_item_done(self, item_id: int, lang: str = "en") -> Response:
        """Mark to-do item as DONE userToDoListItemId"""
        return self._request(
            method="PATCH",
            endpoint=f"/{item_id}",
            params={"lang": lang}
        )

    @allure.step("Update status of to-do item userToDoListItemId={item_id} to {status}")
    def update_item_status(self, item_id: int, status: str, lang: str = "en") -> Response:
        """Update status of to-do item userToDoListItemId"""
        return self._request(
            method="PATCH",
            endpoint=f"/{item_id}/status/{status}",
            params={"lang": lang}
        )

    # ===================== DELETE =====================

    @allure.step("Delete one to-do item habitId={habit_id}, itemId={item_id}")
    def delete_todo_item(self, habit_id: int, item_id: int) -> Response:
        """Delete one to-do item habitId"""
        return self._request(
            method="DELETE",
            endpoint="",
            params={
                "habitId": habit_id,
                "toDoListItemId": item_id
            }
        )

    @allure.step("Delete multiple to-do items ids={ids}")
    def delete_multiple_items(self, ids: list[int]) -> Response:
        """Delete multiple to-do items ids"""
        ids_str = ",".join(map(str, ids))
        return self._request(
            method="DELETE",
            endpoint="/user-to-do-list-items",
            params={"ids": ids_str}
        )

    @allure.step("Get all habits for current user")
    def get_habits(self, lang="en"):
        """
        Returns list of habits for current user.
        """
        return self._request(
            method="GET",
            endpoint="/habit",
            params={"lang": lang}
        )
