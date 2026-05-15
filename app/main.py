from fastapi import Depends,FastAPI
from typing import Annotated
from app.core.security import oauth2_scheme
from app.models.auth import fake_decode_token,User



app = FastAPI()

@app.get("/api/v1")
async def read_root(token : Annotated[str, Depends(oauth2_scheme)]):
    return {"Hello": "World"}


async def get_current_user(token : Annotated[str, Depends(oauth2_scheme)]):
    user = fake_decode_token(token)
    return user

@app.get("users/me")
async def read_users_me(current_user: Annotated[User, Depends(get_current_user)]):
    return current_user