from fastapi import FastAPI

from routers.user.router import router as user_router
from routers.product.router import router as product_router
from routers.message.router import router as message_router
from routers.comment.router import router as comment_router


app = FastAPI()

app.include_router(user_router, tags=['users'])
app.include_router(product_router, tags=['product'])
app.include_router(message_router, tags=['message'])
app.include_router(comment_router, tags=['comment'])
