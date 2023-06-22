from sqlalchemy.orm import Session

from api.Product.ProductAPI import ProductAPI
from services.Base.BaseServiceClass import BaseServiceClass


class ProductService(BaseServiceClass):
    @staticmethod
    def create(session: Session, owner_id: int, description: str, title: str, image_url: str):
        ProductAPI.create(session, owner_id, description, title, image_url)
        session.commit()

    @staticmethod
    def read_all(session: Session):
        return ProductAPI.read_all(session)

    @staticmethod
    def read_by_id(session: Session, id_: int):
        return ProductAPI.read_by_id(session, id_)

    @staticmethod
    def update_by_id(
            session: Session,
            id_: int,
            new_owner_id: int | None,
            new_description: str | None,
            new_title: str | None,
            new_image_url: str | None
    ):
        ProductAPI.update_by_id(
            session,
            id_,
            new_owner_id,
            new_description,
            new_title,
            new_image_url
        )
        session.commit()

    @staticmethod
    def delete_by_id(session: Session, id_: int):
        ProductAPI.delete_by_id(session, id_)
        session.commit()
