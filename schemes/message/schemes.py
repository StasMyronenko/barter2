from ..base.schemes import BaseCreatingSchema, BaseSchema


class MessageCreateSchema(BaseCreatingSchema):
    from_id: int
    to_id: int
    message: str
    date: str | None


class MessageSchema(BaseSchema, MessageCreateSchema):
    pass


class MessageUpdateSchema(BaseSchema):
    new_from_id: int | None
    new_to_id: int | None
    new_message: str | None
    new_date: str | None
