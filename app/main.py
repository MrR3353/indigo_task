from fastapi import FastAPI

from routes.user_router import router as user_router
from routes.movie_router import router as movie_router
from routes.favorite_router import router as favorite_router

app = FastAPI()

app.include_router(user_router)
app.include_router(movie_router)
app.include_router(favorite_router)