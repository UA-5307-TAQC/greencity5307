"""Client for interacting with the Eco News API, extending BaseClient for common functionality."""

import allure
from requests import Response

from clients.base_client import BaseClient


class EcoNewClient(BaseClient):
    """Client for interacting with the Eco News API,
     extending BaseClient for common functionality."""

    def __init__(self, base_url, access_token=None):
        """Client for interacting with the Eco News API,
        extending BaseClient for common functionality."""
        super().__init__(base_url=f"{base_url}/eco-news",
                         access_token=access_token)

    @allure.step(
        "Find eco news by page with filters: tags={tags}, title={title}, "
        "author_id={author_id}, favorite={favorite}, page={page}, size={size}, "
        "sort={sort}")
    def find_eco_news_by_page(self,
                              # pylint: disable=too-many-arguments, too-many-positional-arguments
                              tags: list[str] = None,
                              title: str = None,
                              author_id: int = None,
                              favorite: bool = False,
                              page: int = 0,
                              size: int = 20,
                              sort: list[str] = None) -> Response:
        """Find eco news by page with optional filters and sorting."""
        params = {
            "favorite": favorite,
            "page": page,
            "size": size,
        }
        if tags:
            params["tags"] = ",".join(tags)
        if title:
            params["title"] = title
        if author_id:
            params["authorId"] = author_id
        if sort:
            params["sort"] = ",".join(sort)

        return self._request("GET", "", params=params)

    @allure.step("Find one eco news by {news_id} with filters: lang={lang}")
    def find_eco_news_by_id(self, news_id: int, lang: str = None) -> Response:
        """Find one eco news by id with optional filters."""
        params = {}
        if lang:
            params["lang"] = lang

        return self._request("GET", f"/{news_id}", params=params)


    @allure.step("Like/remove like at eco new by id.")
    def like_remove_like_eco_new_by_id(self, news_id):
        """Check like or remove like for eco new by id"""
        params = {
            "ecoNewsId": news_id
        }
        return self._request("POST", f"/{news_id}/likes", params=params)

    @allure.step("Check if user liked eco new request")
    def user_like_eco_news_by_id(self, news_id, user_id) -> Response:
        """Check if user liked eco new"""
        params = {
            "ecoNewsId" : news_id,
            "userId" : user_id
        }
        return self._request("GET", f"/{news_id}/likes/{user_id}", params=params)
