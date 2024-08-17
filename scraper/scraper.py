from requests import get, Response
from typing import Any


class Scraper:
    def __init__(self, url: str = "") -> None:
        self.__url: str = url
        self.__response: Response
        self.__get_request()

    def set_url(self, url: str) -> None:
        self.__url = url
        self.__get_request()

    def get_current_url(self) -> str:
        return self.__url

    def __get_request(self) -> None:
        self.__response = get(self.__url)

    def get_request_content(self) -> str:
        return self.__response.text

    def get_request_headers(self) -> Any:
        """returns a dict[str,str]. Any because of special internal types"""
        return self.__response.headers


if __name__ == "__main__":
    res: dict[str, str] = Scraper(
        "https://pypi.org/project/requests"
    ).get_request_headers()
    print(res["Connection"])
