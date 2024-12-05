from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from models import Favorite
from repositories.movie_repo import MovieRepository
from repositories.user_repo import UserRepository
from schemas import FavoriteBase


class FavoriteRepository:

    @staticmethod
    async def get(data: FavoriteBase, db: AsyncSession) -> Favorite:
        filter_data = data.dict(exclude_unset=True)
        result = await db.execute(select(Favorite).filter_by(**filter_data))
        obj = result.scalars().first()
        # if not obj:
        #     raise HTTPException(status_code=404, detail="Favorite not found")
        return obj

    @staticmethod
    async def get_user_favorites(user_id: int, db: AsyncSession) -> list[Favorite]:
        query = select(Favorite).filter(Favorite.user_id == user_id).options(selectinload(Favorite.movie))
        result = await db.execute(query)
        return list(result.scalars().all())

    @staticmethod
    async def create(data: FavoriteBase, db: AsyncSession) -> Favorite:
        user = await UserRepository.get(data.user_id, db)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        movie = await MovieRepository.get(data.movie_id, db)
        if not movie:
            raise HTTPException(status_code=404, detail="Movie not found")
        favorite = FavoriteRepository.get(data, db)
        if favorite:
            raise HTTPException(status_code=400, detail="This movie is already in the user's favorites")
        obj = Favorite(**data.dict())
        db.add(obj)
        await db.commit()
        await db.refresh(obj)
        return obj

    @staticmethod
    async def delete(data: FavoriteBase, db: AsyncSession) -> None:
        filter_data = data.dict(exclude_unset=True)
        query = select(Favorite).filter_by(**filter_data)
        result = await db.execute(query)
        favorite = result.scalars().first()
        if favorite:
            await db.delete(favorite)
            await db.commit()
        else:
            raise HTTPException(status_code=404, detail="Favorite not found")
