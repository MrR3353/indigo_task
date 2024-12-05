from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from services.user_service import UserService
from database import get_async_session
from schemas import UserBase, UserResponse

router = APIRouter(prefix='/users')


@router.get("/{user_id}", response_model=UserResponse, summary="Возвращает пользователя по id")
async def get_user(user_id: int, db: AsyncSession = Depends(get_async_session)):
    return await UserService.get_user_by_id(user_id, db)


@router.post("/", response_model=UserResponse, summary="Создает нового пользователя")
async def create_user(user_data: UserBase, db: AsyncSession = Depends(get_async_session)):
    return await UserService.create_user(user_data, db)


@router.put("/{user_id}", response_model=UserResponse, summary="Обновляет данные пользователя")
async def update_user(user_id: int, updates: UserBase, db: AsyncSession = Depends(get_async_session)):
    return await UserService.update_user(user_id, updates, db)


@router.delete("/{user_id}", summary="Удаляет пользователя по id")
async def delete_user(user_id: int, db: AsyncSession = Depends(get_async_session)):
    return await UserService.delete_user(user_id, db)
