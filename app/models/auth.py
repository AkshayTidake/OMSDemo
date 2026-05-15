from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    email: str
    fullname:str
    is_active: bool

def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", 
        email=token + "fakedecoded@example.com", 
        fullname=token + "fakedecoded", 
        is_active=True)
    