from sqlalchemy.ext.asyncio import AsyncSession
from repositories.favorite_repo import FavoriteRepository
from schemas import FavoriteBase, FavoriteResponse


class FavoriteService:
    @staticmethod
    async def create(data: FavoriteBase, db: AsyncSession) -> FavoriteResponse:
        return await FavoriteRepository.create(data, db)

    @staticmethod
    async def delete(data: FavoriteBase, db: AsyncSession):
        return await FavoriteRepository.delete(data, db)

    @staticmethod
    async def get_user_favorites(user_id: int, db: AsyncSession) -> list[FavoriteResponse]:
        return await FavoriteRepository.get_user_favorites(user_id, db)
