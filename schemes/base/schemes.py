from pydantic import BaseModel


class BaseCreatingSchema(BaseModel):
    pass


class BaseSchema(BaseModel):
    id: int
