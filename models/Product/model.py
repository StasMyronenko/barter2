from sqlalchemy import Integer, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.Base.model import Base
from models.User.model import User


class Product(Base):
    __tablename__ = 'product'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    owner_id: Mapped[id] = mapped_column(ForeignKey(f'{User.__tablename__}.{User.id.key}'))
    owner: Mapped[User] = relationship(User)

    description: Mapped[str] = mapped_column(String)
    title: Mapped[str] = mapped_column(String, nullable=False)
    imageURL: Mapped[str] = mapped_column(String)
