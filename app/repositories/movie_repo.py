from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models import Movie
from schemas import MovieBase


class MovieRepository:
    @staticmethod
    async def get(movie_id: int, db: AsyncSession) -> Movie:
        result = await db.execute(select(Movie).filter(Movie.id == movie_id))
        obj = result.scalars().first()
        if not obj:
            raise HTTPException(status_code=404, detail="Movie not found")
        return obj

    @staticmethod
    async def create(data: MovieBase, db: AsyncSession) -> Movie:
        obj = Movie(**data.dict())
        db.add(obj)
        await db.commit()
        await db.refresh(obj)
        return obj

    @staticmethod
    async def delete(movie_id: int, db: AsyncSession) -> None:
        obj = await MovieRepository.get(movie_id, db)
        await db.delete(obj)
        await db.commit()

    @staticmethod
    async def update(movie_id: int, data: MovieBase, db: AsyncSession) -> Movie:
        obj = await MovieRepository.get(movie_id, db)
        updates_dict = data.dict(exclude_unset=True)
        for field, value in updates_dict.items():
            setattr(obj, field, value)

        await db.commit()
        await db.refresh(obj)
        return obj

