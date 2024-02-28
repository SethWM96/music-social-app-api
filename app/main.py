from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List


import db from SessionLocal

from models.account import Account

# FastAPI app
app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


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
