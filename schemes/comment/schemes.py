from ..base.schemes import BaseCreatingSchema, BaseSchema


class CommentCreateSchema(BaseCreatingSchema):
    from_user_id: int
    product_id: int
    message: str


class CommentSchema(BaseSchema, CommentCreateSchema):
    pass


class CommentUpdateSchema(BaseSchema):
    new_from_user_id: int | None
    new_product_id: int | None
    new_message: str | None
