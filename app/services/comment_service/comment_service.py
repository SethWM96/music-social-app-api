import comment_service_interface as comment_service_interface
from models import Comment, comment_create
from collections import List

class CommentService(comment_service_interface):
    def __init__(self, comment_repo):
        self.comment_repo = comment_repo

    # def get_comment(self, comment_id: int) -> Optional[Comment]:
    #     comment = self.comment_repo.get_comment_by_id(comment_id)
    #     if not comment:
    #         raise HTTPException(status_code=404, detail="Comment not found")
    #     return comment

    def get_comments(self) -> List[Comment]:
        return self.comment_repo.get_all_comments()

    # def create_comment(self, comment_create: CommentCreate) -> Comment:
    #     # Validate comment_create data
    #     # Optionally perform any business logic checks before creating the comment
    #     comment = self.comment_repo.create_comment(comment_create)
    #     return comment

    # def update_comment(self, comment_id: int, comment_update: CommentUpdate) -> Comment:
    #     # Check if the comment exists
    #     existing_comment = self.get_comment(comment_id)
        
    #     # Update the existing comment with new data
    #     updated_comment = self.comment_repo.update_comment(comment_id, comment_update)
    #     return updated_comment

    # def delete_comment(self, comment_id: int) -> None:
    #     # Check if the comment exists
    #     existing_comment = self.get_comment(comment_id)
        
    #     # Delete the comment
    #     self.comment_repo.delete_comment(comment_id)
