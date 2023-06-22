from sqlalchemy.orm import Session

from api.Comment.CommentAPI import CommentAPI
from services.Base.BaseServiceClass import BaseServiceClass


class CommentService(BaseServiceClass):
    @staticmethod
    def create(
            session: Session,
            from_user_id: int,
            product_id: int,
            message: str
    ):
        CommentAPI.create(
            session,
            from_user_id,
            product_id,
            message
        )
        session.commit()

    @staticmethod
    def read_all(session: Session):
        return CommentAPI.read_all(session)

    @staticmethod
    def read_by_id(session: Session, id_: int):
        return CommentAPI.read_by_id(session, id_)

    @staticmethod
    def update_by_id(
            session: Session,
            id_: int,
            new_from_user_id: int | None,
            new_product_id: int | None,
            new_message: str | None,
    ):
        CommentAPI.update_by_id(
            session,
            id_,
            new_from_user_id,
            new_product_id,
            new_message,
        )
        session.commit()

    @staticmethod
    def delete_by_id(session: Session, id_: int):
        CommentAPI.delete_by_id(session, id_)
        session.commit()
