from fastapi import FastAPI
from routers.posts import router as posts_router

app = FastAPI()
print("start fastapi123")
app.include_router(posts_router)
