from ..base.schemes import BaseCreatingSchema, BaseSchema


class ProductCreateSchema(BaseCreatingSchema):
    owner_id: int
    description: str
    title: str
    image_url: str


class ProductSchema(BaseSchema, ProductCreateSchema):
    pass


class ProductUpdateSchema(BaseSchema):
    new_owner_id: int | None
    new_description: str | None
    new_title: str | None
    new_image_url: str | None
