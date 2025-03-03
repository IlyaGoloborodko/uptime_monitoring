from typing import Literal

from fastapi import FastAPI

from .monitoring.services.ping import Ping


app = FastAPI()

@app.get("/ping/")
async def ping_url(url: str,
                   method: Literal['get', 'post', 'put', 'delete'],
                   ) -> dict:
    ping = Ping(url=url, method=method)
    result = await ping.process()
    return dict(result=result)
