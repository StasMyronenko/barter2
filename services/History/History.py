from sqlalchemy.orm import Session

from api.History.HistoryAPI import HistoryAPI
from services.Base.BaseServiceClass import BaseServiceClass


class HistoryService(BaseServiceClass):
    @staticmethod
    def create(
            session: Session,
            product_id: int,
            to_user_id: int,
            is_accepted: bool
    ):
        HistoryAPI.create(
            session,
            product_id,
            to_user_id,
            is_accepted
    )
        session.commit()

    @staticmethod
    def read_all(session: Session):
        return HistoryAPI.read_all(session)

    @staticmethod
    def read_by_id(session: Session, id_: int):
        return HistoryAPI.read_by_id(session, id_)

    @staticmethod
    def update_by_id(
            session: Session,
            id_: int,
            new_product_id: int | None,
            new_to_user_id: int | None,
            new_is_accepted: bool | None
    ):
        HistoryAPI.update_by_id(
            session,
            id_,
            new_product_id,
            new_to_user_id,
            new_is_accepted
        )
        session.commit()

    @staticmethod
    def delete_by_id(session: Session, id_: int):
        HistoryAPI.delete_by_id(session, id_)
        session.commit()
