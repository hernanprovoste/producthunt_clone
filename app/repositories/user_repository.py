from sqlalchemy.orm import Session
from .. import models
from .. import schemas
from .. import security

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_email(self, email: str) -> models.User:
        return self.db.query(models.User).filter(models.User.email == email).first()

    def create_user(self, user: schemas.UserCreate) -> models.User:
        hashed_password = security.get_password_hash(user.password)
        db_user = models.User(email=user.email, hashed_password=hashed_password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user