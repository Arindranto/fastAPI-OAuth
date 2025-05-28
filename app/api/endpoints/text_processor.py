from fastapi import APIRouter, Depends, HTTPException, status
from app.models.schemas import TextInput, WordListResponse
from app.services.text_service import tokenize_text
from app.api.dependencies import get_current_user
from typing import Dict

router = APIRouter()

@router.post("/tokenize", response_model=WordListResponse)
async def process_text(
    text_input: TextInput,
    current_user: Dict = Depends(get_current_user) # Protect this endpoint with JWT
):
    """
    Endpoint to tokenize input text into a list of words.
    Requires a valid JWT access token.
    """
    # Log the authenticated user (for demonstration)
    print(f"Request received from user: {current_user['username']}")

    words = tokenize_text(text_input.text)
    return {"words": words}