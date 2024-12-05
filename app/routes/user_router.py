from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from services.user_service import UserService
from database import get_async_session
from schemas import UserBase, UserResponse

router = APIRouter(prefix='/users')


@router.get("/{user_id}", response_model=UserResponse, summary="Возвращает пользователя по id")
async def get(user_id: int, db: AsyncSession = Depends(get_async_session)):
    return await UserService.get(user_id, db)


@router.post("/", response_model=UserResponse, summary="Создает нового пользователя")
async def create(data: UserBase, db: AsyncSession = Depends(get_async_session)):
    return await UserService.create(data, db)


@router.put("/{user_id}", response_model=UserResponse, summary="Обновляет данные пользователя")
async def update(user_id: int, data: UserBase, db: AsyncSession = Depends(get_async_session)):
    return await UserService.update(user_id, data, db)


@router.delete("/{user_id}", summary="Удаляет пользователя по id")
async def delete(user_id: int, db: AsyncSession = Depends(get_async_session)):
    return await UserService.delete(user_id, db)
