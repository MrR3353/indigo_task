from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from services.movie_service import MovieService
from database import get_async_session
from schemas import MovieBase, MovieResponse

router = APIRouter(prefix='/movie', tags=['Movie'])


@router.get("/{movie_id}", response_model=MovieResponse, summary="Возвращает фильм по id")
async def get(movie_id: int, db: AsyncSession = Depends(get_async_session)):
    return await MovieService.get(movie_id, db)


@router.post("/", response_model=MovieResponse, summary="Создает новый фильм")
async def create(data: MovieBase, db: AsyncSession = Depends(get_async_session)):
    return await MovieService.create(data, db)


@router.put("/{movie_id}", response_model=MovieResponse, summary="Обновляет данные фильма")
async def update(movie_id: int, data: MovieBase, db: AsyncSession = Depends(get_async_session)):
    return await MovieService.update(movie_id, data, db)


@router.delete("/{movie_id}", summary="Удаляет пользователя по id")
async def delete(movie_id: int, db: AsyncSession = Depends(get_async_session)):
    return await MovieService.delete(movie_id, db)
