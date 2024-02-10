from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Comment(BaseModel):
    comment_id: int
    account_id: int
    comment_content: str
    like_count: int
    dislike_count: int
    created_on: datetime
    updated_on: datetime
