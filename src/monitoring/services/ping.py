from typing import Literal

from httpx import AsyncClient
# import Exceptions
from httpx import RequestError, HTTPStatusError


class Ping:
    def __init__(self,
                 url: str,
                 method: Literal['get', 'post', 'put', 'delete'],
                 params: dict = None):
        self.url = self.safe_url(url=url)
        self.method = method
        self.params = params if params else {}

    async def process(self):
        try:
            async with AsyncClient() as client:
                return await self.request(client)
        except Exception as e:
            return {'error': str(e)}

    async def request(self,
                      client: AsyncClient):
        http_method = getattr(client, self.method)
        try:
            response = await http_method(url=self.url, params=self.params)
            response.raise_for_status()
            result = dict(
                status_code=response.status_code,
            )
        except RequestError as exc:
            result = dict(
                error=str(exc),
            )
        except HTTPStatusError as exc:
            result = dict(
                status_code=exc.response.status_code,
                error=str(exc),
            )

        return result

    @staticmethod
    def safe_url(url: str) -> str:
        if not url.startswith(('http://', 'https://')):
            return f'https://{url}'
        return url
