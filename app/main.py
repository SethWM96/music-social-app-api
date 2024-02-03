from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from typing import List

# Replace these values with your own PostgreSQL connection details
DATABASE_URL = "postgresql://postgres:ABCD1234@localhost:5432/music_recommendation_app"


# SQLAlchemy configuration
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Define SessionLocal
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# FastAPI app
app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# SQLAlchemy model
class Account(Base):
    __tablename__ = "account"
    account_id = Column(Integer, Sequence('account_id_seq'), primary_key=True, index=True)
    account_name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

# Create tables in the database
Base.metadata.create_all(bind=engine)

# Pydantic model for request and response
class AccountRequest(BaseModel):
    account_name: str
    email: str
    password: str

class AccountResponse(BaseModel):
    account_id: int
    account_name: str
    email: str

# Routes
@app.post("/accounts/", response_model=AccountResponse)
def create_account(account: AccountRequest, db: Session = Depends(get_db)):
    db_account = Account(**account.dict())
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return db_account

@app.get("/accounts" , response_model=List[AccountResponse])
def get_all_accounts(db: Session = Depends(get_db)):
    accounts =  db.query(Account).all()
    # return accounts
    return accounts

@app.get("/accounts/{account_id}", response_model=AccountResponse)
def read_account(account_id: int, db: Session = Depends(get_db)):
    account = db.query(Account).filter(Account.id == account_id).first()
    if account is None:
        raise HTTPException(status_code=404, detail="Account not found")
    return AccountResponse(id=account.id, username=account.username, email=account.email)
