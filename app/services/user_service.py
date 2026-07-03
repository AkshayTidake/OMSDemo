from app.models.user import User
from OMSDemo.app.repositories.user_repository import UserRepository


class UserService:

    def __init__(self,db):

        self.db = db
        self.user_repo = UserRepository(db)