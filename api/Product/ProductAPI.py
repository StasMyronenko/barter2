from typing import Type

from sqlalchemy import Sequence, select
from sqlalchemy.orm import Session

from api.Base.BaseAPI import BaseAPI
from models.Product.model import Product


class ProductAPI(BaseAPI):
    @staticmethod
    def create(session: Session, owner_id: int, description: str, title: str, image_url: str):
        product = Product(owner_id=owner_id, description=description, title=title, imageURL=image_url)
        session.add(product)

    @staticmethod
    def read_all(session: Session) -> Sequence["Product"]:
        statement = select(Product)
        products = session.scalars(statement).all()
        return products

    @staticmethod
    def read_by_id(session: Session, id_: int) -> Type["Product"] | None:
        product = session.get(Product, id_)
        return product

    @staticmethod
    def update_by_id(
            session: Session,
            id_: int,
            new_owner_id: int | None,
            new_description: str | None,
            new_title: str | None,
            new_image_url: str | None
    ):
        product = session.get(Product, id_)
        if new_owner_id:
            product.owner_id = new_owner_id
        if new_description:
            product.description = new_description
        if new_title:
            product.title = new_title
        if new_image_url:
            product.imageURL = new_image_url

    @staticmethod
    def delete_by_id(session: Session, id_: int) -> None:
        product = session.get(Product, id_)
        session.delete(product)
