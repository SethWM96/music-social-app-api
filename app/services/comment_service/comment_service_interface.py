from abc import ABC, abstractmethod
from typing import List, Optional
from models import Comment, CommentCreate, CommentUpdate   

class CommentServiceInterface(ABC):
    @abstractmethod
    def get_comment(self, comment_id: int) -> Optional[Comment]:
        pass

    @abstractmethod
    def get_comments(self) -> List[Comment]:
        pass

    @abstractmethod
    def create_comment(self, data: CommentCreate) -> Comment:
        pass

    @abstractmethod
    def update_comment(self, comment_id: int, data: CommentUpdate) -> Comment:
        pass

    @abstractmethod
    def delete_comment(self, comment_id: int) -> None:
        pass



