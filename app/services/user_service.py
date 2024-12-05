from sqlalchemy.ext.asyncio import AsyncSession
from schemas import UserBase, UserResponse
from repositories.user_repo import UserRepository


class UserService:
    @staticmethod
    async def get_user_by_id(user_id: int, db: AsyncSession) -> UserResponse:
        user = await UserRepository.get_user_by_id(user_id, db)
        return UserResponse.from_orm(user)

    @staticmethod
    async def create_user(user_data: UserBase, db: AsyncSession) -> UserResponse:
        user = await UserRepository.create_user(user_data, db)
        return UserResponse.from_orm(user)

    @staticmethod
    async def update_user(user_id: int, updates: UserBase, db: AsyncSession) -> UserResponse:
        user = await UserRepository.update_user(user_id, updates, db)
        return UserResponse.from_orm(user)

    @staticmethod
    async def delete_user(user_id: int, db: AsyncSession) -> None:
        return await UserRepository.delete_user(user_id, db)
