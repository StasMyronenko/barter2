from ..base.schemes import BaseCreatingSchema, BaseSchema


class UserCreateSchema(BaseCreatingSchema):
    name: str
    number: str


class UserSchema(BaseSchema, UserCreateSchema):
    pass


class UserUpdateSchema(BaseSchema):
    new_name: str | None
    new_number: str | None
