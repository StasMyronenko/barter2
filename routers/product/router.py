from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemes.product.schemes import ProductCreateSchema, ProductUpdateSchema
from services.Product.service import ProductService
from utils.db.get_db_session import get_db_session

router = APIRouter(prefix="/products")


@router.post("/create")
async def create_product(product: ProductCreateSchema, session: Annotated[Session, Depends(get_db_session)]):
    ProductService.create(
        session,
        product.owner_id,
        product.description,
        product.title,
        product.image_url,
    )
    return {"status": "created"}


@router.get("/all")
async def read_all_products(session: Annotated[Session, Depends(get_db_session)]):
    products = ProductService.read_all(session)
    return {"products": products}


@router.get("/{product_id}")
async def read_product_by_id(product_id: int, session: Annotated[Session, Depends(get_db_session)]):
    product = ProductService.read_by_id(session, product_id)
    return {"product": product}


@router.post("/update")
async def update_product_by_id(product: ProductUpdateSchema, session: Annotated[Session, Depends(get_db_session)]):
    ProductService.update_by_id(
        session,
        product.id,
        product.new_owner_id,
        product.new_description,
        product.new_title,
        product.new_image_url,
    )
    return {"status": "updated"}


@router.delete("/delete/{product_id}")
async def delete_product(product_id: int, session: Annotated[Session, Depends(get_db_session)]):
    ProductService.delete_by_id(session, product_id)
    return {"status": "deleted"}
