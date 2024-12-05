from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import User


class UserRepository:
    @staticmethod
    async def get_user_by_id(db: AsyncSession, user_id: int):
        result = await db.execute(select(User).filter(User.id == user_id))
        return result.scalars().first()

    @staticmethod
    async def create_user(db: AsyncSession, user: User):
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user

    @staticmethod
    async def delete_user(db: AsyncSession, user: User):
        await db.delete(user)
        await db.commit()

    @staticmethod
    async def update_user(db: AsyncSession, user: User, name: str = None, email: str = None):
        if name:
            user.name = name
        if email:
            user.email = email

        if not name and not email:
            return user  # Ничего не обновляем, возвращаем текущий объект

        db.add(user)  # Добавляем пользователя в сессию (хотя он уже там, это безопасно)
        await db.commit()
        await db.refresh(user)  # Обновляем данные пользователя из базы
        return user

