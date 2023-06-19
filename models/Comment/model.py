from sqlalchemy import Integer, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from models.Base.model import Base
from models.Product.model import Product
from models.User.model import User


class Comment(Base):
    __tablename__ = 'comment'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    from_user_id: Mapped[int] = mapped_column(ForeignKey(f'{User.__tablename__}.{User.id.key}'))
    from_user: Mapped[User] = relationship()

    product_id: Mapped[int] = mapped_column(ForeignKey(f'{Product.__tablename__}.{Product.id.key}'))
    product: Mapped[Product] = relationship()

    message = mapped_column(String)
