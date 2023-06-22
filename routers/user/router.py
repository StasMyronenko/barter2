from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemes.user.schemes import UserCreateSchema, UserUpdateSchema
from services.User.service import UserService
from utils.db.get_db_session import get_db_session

router = APIRouter(prefix="/users")


@router.post("/create")
async def create_user(user: UserCreateSchema, session: Annotated[Session, Depends(get_db_session)]):
    UserService.create(session, user.name, user.number)
    return {"status": "created"}


@router.get("/all")
async def read_all_users(session: Annotated[Session, Depends(get_db_session)]):
    users = UserService.read_all(session)
    return {"users": users}


@router.get("/{user_id}")
async def read_user_by_id(user_id: int, session: Annotated[Session, Depends(get_db_session)]):
    user = UserService.read_by_id(session, user_id)
    return {"user": user}


@router.post("/update")
async def update_user_by_id(user: UserUpdateSchema, session: Annotated[Session, Depends(get_db_session)]):
    UserService.update_by_id(session, user.id, user.new_name, user.new_number)
    return {"status": "updated"}


@router.delete("/delete/{user_id}")
async def delete_user(user_id: int, session: Annotated[Session, Depends(get_db_session)]):
    UserService.delete_by_id(session, user_id)
    return {"status": "deleted"}
