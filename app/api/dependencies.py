from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.security import decode_access_token
from typing import Optional, Generator

from app.models.database import SessionLocal

# OAuth2PasswordBearer is used to extract the token from the Authorization header
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

# Dependency to get a database session for each request
def get_db() -> Generator[Session, None, None]:
    """
    Provides a SQLAlchemy database session for each request.
    Ensures the session is closed after the request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_current_user(token: str = Depends(oauth2_scheme)) -> Optional[dict]:
    """
    Dependency to get the current authenticated user from the JWT token.
    Raises HTTPException if the token is invalid or expired.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = decode_access_token(token)
    if payload is None:
        raise credentials_exception
    # You might want to fetch user details from a database here
    # For this example, we just return the payload (e.g., {"sub": "username"})
    sub = payload.get("sub")
    if sub is None:
        raise credentials_exception
    return {"username": sub} # In a real app, this would be a User object