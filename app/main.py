from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .databaase import engine
from . routers import user, post, auth, vote
from . config import Settings

#models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Hello"}

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


