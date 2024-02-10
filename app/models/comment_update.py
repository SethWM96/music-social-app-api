from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class CommentUpdate(BaseModel):
    comment_content: Optional[str]
    like_count: Optional[str]
    dislike_count: Optional[str]
    updated_on: Optional[datetime]
