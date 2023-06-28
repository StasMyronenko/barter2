from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemes.history.schemes import HistoryCreateSchema, HistoryUpdateSchema
from services.History.service import HistoryService
from utils.db.get_db_session import get_db_session

router = APIRouter(prefix="/history")


@router.post("/create")
async def create_history(history: HistoryCreateSchema, session: Annotated[Session, Depends(get_db_session)]):
    HistoryService.create(session, **history.dict())
    return {"status": "created"}


@router.get("/all")
async def read_all_historys(session: Annotated[Session, Depends(get_db_session)]):
    historys = HistoryService.read_all(session)
    return {"historys": historys}


@router.get("/{history_id}")
async def read_history_by_id(history_id: int, session: Annotated[Session, Depends(get_db_session)]):
    history = HistoryService.read_by_id(session, history_id)
    return {"history": history}


@router.post("/update")
async def update_history_by_id(history: HistoryUpdateSchema, session: Annotated[Session, Depends(get_db_session)]):
    history_dict = history.dict()
    history_dict['id_'] = history_dict['id']
    del history_dict['id']
    HistoryService.update_by_id(session, **history_dict)
    return {"status": "updated"}


@router.delete("/delete/{history_id}")
async def delete_history(history_id: int, session: Annotated[Session, Depends(get_db_session)]):
    HistoryService.delete_by_id(session, history_id)
    return {"status": "deleted"}
