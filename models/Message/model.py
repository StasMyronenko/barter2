from sqlalchemy import Integer, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.Base.model import Base
from models.User.model import User


class Message(Base):
    __tablename__ = 'message'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    from_id: Mapped[id] = mapped_column(ForeignKey(f'{User.__tablename__}.{User.id.key}'))
    from_user: Mapped[User] = relationship(User, foreign_keys=[from_id])

    to_id: Mapped[id] = mapped_column(ForeignKey(f'{User.__tablename__}.{User.id.key}'))
    to_user: Mapped[User] = relationship(User, foreign_keys=[to_id])

    message: Mapped[str] = mapped_column(String, nullable=False)
    date: Mapped[str] = mapped_column(String)
