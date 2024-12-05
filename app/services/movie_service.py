from sqlalchemy.ext.asyncio import AsyncSession
from schemas import MovieBase, MovieResponse
from repositories.movie_repo import MovieRepository


class MovieService:
    @staticmethod
    async def get(movie_id: int, db: AsyncSession) -> MovieResponse:
        movie = await MovieRepository.get(movie_id, db)
        return MovieResponse.from_orm(movie)

    @staticmethod
    async def create(data: MovieBase, db: AsyncSession) -> MovieResponse:
        movie = await MovieRepository.create(data, db)
        return MovieResponse.from_orm(movie)

    @staticmethod
    async def update(movie_id: int, data: MovieBase, db: AsyncSession) -> MovieResponse:
        movie = await MovieRepository.update(movie_id, data, db)
        return MovieResponse.from_orm(movie)

    @staticmethod
    async def delete(movie_id: int, db: AsyncSession) -> None:
        return await MovieRepository.delete(movie_id, db)
