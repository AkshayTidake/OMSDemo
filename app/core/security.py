from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm

fake_users_db ={
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "is_active": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret",
        "is_active": True,
    }
}
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def fake_hashed_password(password:str):
    return "fakehashed" + password


