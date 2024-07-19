# import sys
# from pathlib import Path
# sys.path.append(str(Path(__file__).resolve().parent.parent))

import uvicorn
from fastapi import APIRouter, FastAPI, Response

from app import settings
from app.server.api.routes.user_routes import router as user_router

app = FastAPI()


app.include_router(user_router)


@app.get("/")
async def root():
    return {"hello": "hi"}


def main(): ...


if __name__ == "__main__":
    uvicorn.run(
        "app.server.main:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=True,
    )
