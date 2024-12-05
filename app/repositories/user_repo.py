from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models import User
from schemas import UserBase


class UserRepository:
    @staticmethod
    async def get(user_id: int, db: AsyncSession) -> User:
        result = await db.execute(select(User).filter(User.id == user_id))
        user = result.scalars().first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user

    @staticmethod
    async def create(data: UserBase, db: AsyncSession) -> User:
        user = User(**data.dict())
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user

    @staticmethod
    async def delete(user_id: int, db: AsyncSession) -> None:
        user = await UserRepository.get(user_id, db)
        await db.delete(user)
        await db.commit()

    @staticmethod
    async def update(user_id: int, data: UserBase, db: AsyncSession) -> User:
        user = await UserRepository.get(user_id, db)
        updates_dict = data.dict(exclude_unset=True)
        for field, value in updates_dict.items():
            setattr(user, field, value)

        await db.commit()
        await db.refresh(user)
        return user

