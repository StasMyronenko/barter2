from typing import Type

from sqlalchemy import select, Sequence
from sqlalchemy.orm import Session

from api.Base.BaseAPI import BaseAPI
from models.User.model import User


class UserAPI(BaseAPI):
    @staticmethod
    def create(session: Session, name: str, number: str):
        user = User(name=name, number=number)
        session.add(user)

    @staticmethod
    def read_all(session: Session) -> Sequence["User"]:
        statement = select(User)
        users = session.scalars(statement).all()
        return users

    @staticmethod
    def read_by_id(session: Session, id_: int) -> Type["User"] | None:
        user = session.get(User, id_)
        return user

    @staticmethod
    def update_by_id(session: Session, id_: int, new_name: str | None, new_number: str | None):
        user = session.get(User, id_)
        if new_name:
            user.name = new_name
        if new_number:
            user.number = new_number

    @staticmethod
    def delete_by_id(session: Session, id_: int) -> None:
        user = session.get(User, id_)
        session.delete(user)
