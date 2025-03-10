from httpx import AsyncClient

from httpx import RequestError, HTTPStatusError

from backend.app.monitoring.models import PingConfig


class Ping(PingConfig):

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
            response = await http_method(url=self.normalized_url, params=self.params)
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

    @property
    def normalized_url(self) -> str:
        if not self.url.startswith(('http://', 'https://')):
            return f'https://{self.url}'
        return self.url
