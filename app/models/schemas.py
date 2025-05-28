from pydantic import BaseModel, Field
from typing import List


# Schema for user login request
class UserLogin(BaseModel):
    """
    Pydantic model for user login credentials.
    """
    username: str = Field(...)
    password: str = Field(...)


# Schema for the JWT token response
class Token(BaseModel):
    """
    Pydantic model for the JWT token response.
    """
    access_token: str
    token_type: str = "bearer"


# Schema for text input request
class TextInput(BaseModel):
    """
    Pydantic model for text input.
    """
    text: str = Field(..., min_length=1)


# Schema for word list response
class WordListResponse(BaseModel):
    """
    Pydantic model for the word list response.
    """
    words: List[str] = Field(...)
