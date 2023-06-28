from ..base.schemes import BaseCreatingSchema, BaseSchema


class HistoryCreateSchema(BaseCreatingSchema):
    product_id: int
    to_user_id: int
    is_accepted: bool


class HistorySchema(BaseSchema, HistoryCreateSchema):
    pass


class HistoryUpdateSchema(BaseSchema):
    new_product_id: int | None
    new_to_user_id: int | None
    new_is_accepted: bool | None
