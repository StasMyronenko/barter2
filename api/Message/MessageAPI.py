from typing import Type

from sqlalchemy import select, Sequence
from sqlalchemy.orm import Session

from models.Message.model import Message


class MessageAPI:
    @staticmethod
    def create(
            session: Session,
            from_id: int,
            to_id: int,
            message: str,
            date: str
    ):
        message = Message(
            from_id=from_id,
            to_id=to_id,
            message=message,
            date=date
        )
        session.add(message)

    @staticmethod
    def read_all(session: Session) -> Sequence["Message"]:
        statement = select(Message)
        messages = session.scalars(statement).all()
        return messages

    @staticmethod
    def read_by_id(session: Session, id_: int) -> Type["Message"] | None:
        message = session.get(Message, id_)
        return message

    @staticmethod
    def update_by_id(
            session: Session,
            id_: int,
            new_from_id: int | None,
            new_to_id: int | None,
            new_message: str | None,
            new_date: str | None
    ):
        message = session.get(Message, id_)
        if new_from_id:
            message.from_id = new_from_id
        if new_to_id:
            message.to_id = new_to_id
        if new_message:
            message.message = new_message
        if new_date:
            message.date = new_date

    @staticmethod
    def delete_by_id(session: Session, id_: int) -> None:
        message = session.get(Message, id_)
        session.delete(message)
