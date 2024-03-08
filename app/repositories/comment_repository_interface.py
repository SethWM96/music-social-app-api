from abc import ABC, abstractmethod
from typing import List, Optional
from app.models import Comment

class CommentRepositoryInterface(ABC):
    @abstractmethod
    async def get_comment_by_id(self, comment_id: int) -> Optional[Comment]:
        """
        Retrieve a comment by its ID.
        """
        pass

    @abstractmethod
    async def get_all_comments(self) -> List[Comment]:
        """
        Retrieve all comments.
        """
        pass

    @abstractmethod
    async def create_comment(self, comment: Comment) -> Comment:
        """
        Create a new comment.
        """
        pass

    @abstractmethod
    async def update_comment(self, comment_id: int, comment_update: Comment) -> Optional[Comment]:
        """
        Update an existing comment.
        """
        pass

    @abstractmethod
    async def delete_comment(self, comment_id: int) -> None:
        """
        Delete a comment by its ID.
        """
        pass
