from fastapi import FastAPI

from routers.user.router import router as user_router


app = FastAPI()

app.include_router(user_router, tags=['users'])
