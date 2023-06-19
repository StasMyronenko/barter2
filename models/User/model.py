from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from models.Base.model import Base


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    number: Mapped[int] = mapped_column(String, nullable=False, default='')
