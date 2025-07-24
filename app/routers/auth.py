from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session

from .. import schemas, security
from ..database import get_db
from ..repositories.user_repository import UserRepository

# This line says to FastAPI that the URL to get token is /login/
oauth_scheme = OAuth2PasswordBearer(tokenUrl="/login/")

router = APIRouter(
    tags=["Authentication"]
)

@router.post("/register/", response_model=schemas.User)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    user_repository = UserRepository(db)
    db_user = user_repository.get_user_by_email(email = user.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    return user_repository.create_user(user)

@router.post("/login/", response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user_repository = UserRepository(db)
    user = user_repository.get_user_by_email(email=form_data.username) # OAuth2 use username as email

    # Verify that the user exists or the password is correct
    if not user or not security.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Credentials", headers={"WWW-Authenticate": "Bearer"})

    # Create token
    access_token = security.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/users/me/", response_model=schemas.User)
def read_users_me(current_user: schemas.User = Depends(security.get_current_user)):
    return current_user