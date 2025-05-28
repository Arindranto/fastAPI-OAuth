from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

from app.core.config import settings

# For SQLite, 'check_same_thread=False' is needed to allow multiple threads
# to interact with the database connection (necessary for FastAPI's default behavior).
# In a real multi-threaded/multi-process app *using SQLite as a single file*,
# you might need to be careful with write concurrency, but for basic usage it's fine.
engine = create_engine(
    settings.DATABASE_URL, echo=True, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class DBUser(Base):
    """
    SQLAlchemy model for the 'users' table.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    # Optional: You could add more fields like email, full_name, etc.

# This function will create the database tables based on your models
def create_db_tables():
    Base.metadata.create_all(bind=engine)