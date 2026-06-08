from fastapi import Depends,FastAPI
from typing import Annotated
from app.core.security import oauth2_scheme
from app.models.auth import fake_decode_token,User
from contextlib import asynccontextmanager
from app.core.database import engine,Base
from app.models.model import User


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup code: Create database tables
    Base.metadata.create_all(bind=engine)
    print("Database tables created.")
    yield
    # Shutdown code (if needed)
    print("Application shutdown.")

app = FastAPI(lifespan=lifespan)

@app.get("/api/v1")
async def read_root(token : Annotated[str, Depends(oauth2_scheme)]):
    return {"Hello": "World"}


async def get_current_user(token : Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    return user

@app.get("users/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user