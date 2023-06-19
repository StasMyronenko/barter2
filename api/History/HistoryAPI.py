from typing import Type

from sqlalchemy import select, Sequence
from sqlalchemy.orm import Session

from models.History.model import History


class HistoryAPI:
    @staticmethod
    def create(
            session: Session,
            product_id: int,
            to_user_id: int,
            is_accepted: bool
    ):
        history = History(
            product_id=product_id,
            to_user_id=to_user_id,
            is_accepted=is_accepted
        )
        session.add(history)

    @staticmethod
    def read_all(session: Session) -> Sequence["History"]:
        statement = select(History)
        history = session.scalars(statement).all()
        return history

    @staticmethod
    def read_by_id(session: Session, id_: int) -> Type["History"] | None:
        history = session.get(History, id_)
        return history

    @staticmethod
    def update_by_id(
            session: Session,
            id_: int,
            new_product_id: int | None,
            new_to_user_id: int | None,
            new_is_accepted: bool | None
    ):
        history = session.get(History, id_)
        if new_product_id:
            history.product_id = new_product_id
        if new_to_user_id:
            history.to_user_id = new_to_user_id
        if new_is_accepted:
            history.is_accepted = new_is_accepted

    @staticmethod
    def delete_by_id(session: Session, id_: int) -> None:
        history = session.get(History, id_)
        session.delete(history)
