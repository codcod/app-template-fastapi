"""Routes."""

import typing as tp

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from . import db
from .models import User

routes = APIRouter()


@routes.get('/users/{id}', status_code=status.HTTP_200_OK)
async def get_user(
    id: int, session: AsyncSession = Depends(db.get_db_session)
) -> User | tp.Any:
    stmt = select(User).where(User.user_id == id)
    result = await session.exec(stmt)
    user = result.first()
    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    return user


@routes.post('/users')
async def save_user(
    user: User, session: AsyncSession = Depends(db.get_db_session)
) -> User:
    async with session:
        session.add(user)
        await session.commit()
        await session.refresh(user)
    return user
