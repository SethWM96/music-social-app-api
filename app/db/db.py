from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:ABCD1234@localhost:5432/music_recommendation_app"

# SQLAlchemy configuration
engine = create_engine(DATABASE_URL)

# Define SessionLocal
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)