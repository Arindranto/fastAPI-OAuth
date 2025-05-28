# my_microservice/app/main.py
from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.api.endpoints import auth, text_processor
from app.models.database import create_db_tables

# Initialize the FastAPI application
app = FastAPI(
    title="Text Processing Microservice",
    description="A microservice to process text and demonstrate API security with JWT.",
    version="1.0.0"
)



# @asynccontextmanager
# async def lifespan(app: FastAPI):
@app.on_event("startup")
def startup_event():
    create_db_tables()
    print("Database tables created/checked.")
    # Optional: Add an initial user for testing if the DB is empty
    from sqlalchemy.orm import Session
    from app.models.database import SessionLocal, DBUser
    from app.core.security import get_password_hash

    db = SessionLocal()
    try:
        if db.query(DBUser).count() == 0:
            print("No users found. Creating a default testuser.")
            hashed_password = get_password_hash("securepassword") # Hash "securepassword"
            default_user = DBUser(username="testuser", hashed_password=hashed_password)
            db.add(default_user)
            db.commit()
            print("Default 'testuser' created.")
    finally:
        db.close()




# Include API routers from different endpoint modules
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(text_processor.router, prefix="/text", tags=["Text Processing"])

@app.get("/")
async def root():
    """
    Root endpoint for the microservice.
    """
    return {"message": "Welcome to the Text Processing Microservice!"}