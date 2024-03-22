from fastapi import FastAPI
from storeapi.routers.posts import router as posts_router

app = FastAPI()
app.include_router(posts_router)
