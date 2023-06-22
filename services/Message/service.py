from sqlalchemy.orm import Session

from api.Message.MessageAPI import MessageAPI
from services.Base.BaseServiceClass import BaseServiceClass


class MessageService(BaseServiceClass):
    @staticmethod
    def create(
            session: Session,
            from_id: int,
            to_id: int,
            message: str,
            date: str
    ):
        MessageAPI.create(
            session,
            from_id,
            to_id,
            message,
            date
        )
        session.commit()

    @staticmethod
    def read_all(session: Session):
        return MessageAPI.read_all(session)

    @staticmethod
    def read_by_id(session: Session, id_: int):
        return MessageAPI.read_by_id(session, id_)

    @staticmethod
    def update_by_id(
            session: Session,
            id_: int,
            new_from_id: int | None,
            new_to_id: int | None,
            new_message: str | None,
            new_date: str | None
    ):
        MessageAPI.update_by_id(
            session,
            id_,
            new_from_id,
            new_to_id,
            new_message,
            new_date
        )
        session.commit()

    @staticmethod
    def delete_by_id(session: Session, id_: int):
        MessageAPI.delete_by_id(session, id_)
        session.commit()
