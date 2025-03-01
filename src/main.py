from typing import Literal

from fastapi import FastAPI

from src.monitoring.services.ping import Ping

app = FastAPI()


@app.get("/ping/")
async def ping_url(url: str,
                   method: Literal['get', 'post', 'put', 'delete'],
                   params: dict | None = None,
                   ) -> dict:
    ping = Ping(url=url, method=method, params=params)
    result = await ping.process()
    return dict(result=result)
