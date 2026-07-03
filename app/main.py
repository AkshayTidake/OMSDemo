from fastapi import Depends,FastAPI
from typing import Annotated
from contextlib import asynccontextmanager
from app.core.database import engine,Base
from app.models.user import User
from slowapi import Limiter
from OMSDemo.app.api.v1.auth import router as auth_router

limiter = Limiter(key_func=lambda request: request.client.host)

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    

app = FastAPI(lifespan=lifespan)
app.include_router(auth_router)


@app.get("/api/v1")
async def read_root():
    return {"Hello": "World"}


# async def get_current_user(token : Annotated[str, Depends(oauth2_scheme)]):
#     user = fake_decode_token(token)
#     return user

# @app.get("users/me")
# async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
#     return current_user