from sqlalchemy import Integer, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.Base.model import Base
from models.Product.model import Product
from models.User.model import User


class History(Base):
    __tablename__ = 'history'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    product_id: Mapped[id] = mapped_column(ForeignKey(f'{Product.__tablename__}.{Product.id.key}'))
    product: Mapped[Product] = relationship(Product, foreign_keys=[product_id])

    to_user_id: Mapped[id] = mapped_column(ForeignKey(f'{User.__tablename__}.{User.id.key}'))
    to_user: Mapped[User] = relationship(User, foreign_keys=[to_user_id])

    is_accepted: Mapped[bool] = mapped_column(Boolean, nullable=False)
