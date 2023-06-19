from typing import Type

from sqlalchemy import select, Sequence
from sqlalchemy.orm import Session

from models.Comment.model import Comment


class CommentAPI:
    @staticmethod
    def create(
            session: Session,
            from_user_id: int,
            product_id: int,
            message: str
    ):
        comment = Comment(
            from_user_id=from_user_id,
            product_id=product_id,
            message=message
        )
        session.add(comment)

    @staticmethod
    def read_all(session: Session) -> Sequence["Comment"]:
        statement = select(Comment)
        comments = session.scalars(statement).all()
        return comments

    @staticmethod
    def read_by_id(session: Session, id_: int) -> Type["Comment"] | None:
        comment = session.get(Comment, id_)
        return comment

    @staticmethod
    def update_by_id(
            session: Session,
            id_: int,
            new_from_user_id: int | None,
            new_product_id: int | None,
            new_message: str | None,
    ):
        comment = session.get(Comment, id_)
        if new_from_user_id:
            comment.from_user_id = new_from_user_id
        if new_product_id:
            comment.product_id = new_product_id
        if new_message:
            comment.message = new_message

    @staticmethod
    def delete_by_id(session: Session, id_: int) -> None:
        comment = session.get(Comment, id_)
        session.delete(comment)
