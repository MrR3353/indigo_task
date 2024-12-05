from sqlalchemy.ext.asyncio import AsyncSession
from schemas import UserBase, UserResponse
from repositories.user_repo import UserRepository


class UserService:
    @staticmethod
    async def get(user_id: int, db: AsyncSession) -> UserResponse:
        user = await UserRepository.get(user_id, db)
        return UserResponse.from_orm(user)

    @staticmethod
    async def create(data: UserBase, db: AsyncSession) -> UserResponse:
        user = await UserRepository.create(data, db)
        return UserResponse.from_orm(user)

    @staticmethod
    async def update(user_id: int, data: UserBase, db: AsyncSession) -> UserResponse:
        user = await UserRepository.update(user_id, data, db)
        return UserResponse.from_orm(user)

    @staticmethod
    async def delete(user_id: int, db: AsyncSession) -> None:
        return await UserRepository.delete(user_id, db)
