from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Account(Base):
    __tablename__ = "account"
    account_id = Column(Integer, Sequence('account_id_seq'), primary_key=True, index=True)
    account_name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)