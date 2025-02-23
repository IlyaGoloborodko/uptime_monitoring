from fastapi import FastAPI

from src.monitoring.services.ping import ping

app = FastAPI()


@app.get("/ping/")
async def ping_url(
    url: str,
    params: dict | None = None,
):
    return await ping(url=url, params=params or {})
