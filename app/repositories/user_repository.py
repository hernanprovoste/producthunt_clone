from sqlalchemy.orm import Session
from .. import models

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_email(self, email: str) -> models.User:
        """
        Get an user by email
        :param email:
        :return User:
        """
        return self.db.query(models.User).filter(models.User.email == email).first()