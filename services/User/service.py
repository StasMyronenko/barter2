from sqlalchemy.orm import Session

from api.User.UserAPI import UserAPI
from services.Base.BaseServiceClass import BaseServiceClass


class UserService(BaseServiceClass):
    @staticmethod
    def create(session: Session, name: str, number: str):
        UserAPI.create(session, name, number)
        session.commit()

    @staticmethod
    def read_all(session: Session):
        return UserAPI.read_all(session)

    @staticmethod
    def read_by_id(session: Session, id_: int):
        return UserAPI.read_by_id(session, id_)

    @staticmethod
    def update_by_id(session: Session, id_: int, new_name: str | None, new_number: str | None):
        UserAPI.update_by_id(session, id_, new_name, new_number)
        session.commit()

    @staticmethod
    def delete_by_id(session: Session, id_: int):
        UserAPI.delete_by_id(session, id_)
        session.commit()
