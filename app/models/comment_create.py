from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CommentCreate(BaseModel):
    account_id: int
    comment_content: str
    
    
    
