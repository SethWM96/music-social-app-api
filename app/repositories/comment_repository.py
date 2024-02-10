from typing import List, Optional
from app.models import Comment
# from app.db import database

class CommentRepository:
    async def get_comment_by_id(self, comment_id: int) -> Optional[Comment]:
        query = "SELECT * FROM comments WHERE comment_id = :comment_id"
        return await database.fetch_one(query=query, values={"comment_id": comment_id})

    async def get_all_comments(self) -> List[Comment]:
        query = "SELECT * FROM comments"
        return await database.fetch_all(query=query)

    async def create_comment(self, comment: Comment) -> Comment:
        query = """
            INSERT INTO comments (account_id, comment_content, like_count, dislike_count, created_on, updated_on)
            VALUES (:account_id, :comment_content, :like_count, :dislike_count, :created_on, :updated_on)
            RETURNING *
        """
        return await database.fetch_one(query=query, values=comment.dict())

    async def update_comment(self, comment_id: int, comment_update: Comment) -> Optional[Comment]:
        query = """
            UPDATE comments 
            SET 
                account_id = :account_id,
                comment_content = :comment_content,
                like_count = :like_count,
                dislike_count = :dislike_count,
                updated_on = :updated_on
            WHERE comment_id = :comment_id
            RETURNING *
        """
        return await database.fetch_one(query=query, values={**comment_update.dict(), "comment_id": comment_id})

    async def delete_comment(self, comment_id: int) -> None:
        query = "DELETE FROM comments WHERE comment_id = :comment_id"
        await database.execute(query=query, values={"comment_id": comment_id})
