from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemes.comment.schemes import CommentCreateSchema, CommentUpdateSchema
from services.Comment.service import CommentService
from utils.db.get_db_session import get_db_session

router = APIRouter(prefix="/comments")


@router.post("/create")
async def create_comment(comment: CommentCreateSchema, session: Annotated[Session, Depends(get_db_session)]):
    CommentService.create(session, **comment.dict())
    return {"status": "created"}


@router.get("/all")
async def read_all_comments(session: Annotated[Session, Depends(get_db_session)]):
    comments = CommentService.read_all(session)
    return {"comments": comments}


@router.get("/{comment_id}")
async def read_comment_by_id(comment_id: int, session: Annotated[Session, Depends(get_db_session)]):
    comment = CommentService.read_by_id(session, comment_id)
    return {"comment": comment}


@router.post("/update")
async def update_comment_by_id(comment: CommentUpdateSchema, session: Annotated[Session, Depends(get_db_session)]):
    comment_dict = comment.dict()
    comment_dict['id_'] = comment_dict['id']
    del comment_dict['id']
    CommentService.update_by_id(session, **comment_dict)
    return {"status": "updated"}


@router.delete("/delete/{comment_id}")
async def delete_comment(comment_id: int, session: Annotated[Session, Depends(get_db_session)]):
    CommentService.delete_by_id(session, comment_id)
    return {"status": "deleted"}
