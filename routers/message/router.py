from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemes.message.schemes import MessageCreateSchema, MessageUpdateSchema
from services.Message.service import MessageService
from utils.db.get_db_session import get_db_session

router = APIRouter(prefix="/messages")


@router.post("/create")
async def create_message(message: MessageCreateSchema, session: Annotated[Session, Depends(get_db_session)]):
    MessageService.create(session, **message.dict())
    return {"status": "created"}


@router.get("/all")
async def read_all_messages(session: Annotated[Session, Depends(get_db_session)]):
    messages = MessageService.read_all(session)
    return {"messages": messages}


@router.get("/{message_id}")
async def read_message_by_id(message_id: int, session: Annotated[Session, Depends(get_db_session)]):
    message = MessageService.read_by_id(session, message_id)
    return {"message": message}


@router.post("/update")
async def update_message_by_id(message: MessageUpdateSchema, session: Annotated[Session, Depends(get_db_session)]):
    message_dict = message.dict()
    message_dict['id_'] = message_dict['id']
    del message_dict['id']
    MessageService.update_by_id(session, **message_dict)
    return {"status": "updated"}


@router.delete("/delete/{message_id}")
async def delete_message(message_id: int, session: Annotated[Session, Depends(get_db_session)]):
    MessageService.delete_by_id(session, message_id)
    return {"status": "deleted"}
