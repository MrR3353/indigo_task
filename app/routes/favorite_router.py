from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from services.favorite_service import FavoriteService
from database import get_async_session
from schemas import FavoriteBase, FavoriteResponse

router = APIRouter(prefix='/favorites', tags=['Favorite'])


@router.get("/{user_id}", response_model=list[FavoriteResponse], summary="Возвращает избранное пользователя")
async def get_user_favorites(user_id: int, db: AsyncSession = Depends(get_async_session)):
    return await FavoriteService.get_user_favorites(user_id, db)


@router.post("/", response_model=FavoriteResponse, summary="Добавляет фильм в избранное")
async def create(data: FavoriteBase, db: AsyncSession = Depends(get_async_session)):
    return await FavoriteService.create(data, db)


@router.delete("/{user_id}", summary="Удаляет фильм из избранного")
async def delete(data: FavoriteBase, db: AsyncSession = Depends(get_async_session)):
    return await FavoriteService.delete(data, db)
