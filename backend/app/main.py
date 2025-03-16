import uvicorn
from fastapi import FastAPI

from backend.app.api.main import api_router

app = FastAPI()

app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run("backend.app.main:app", host='0.0.0.0', port=80, reload=True)
