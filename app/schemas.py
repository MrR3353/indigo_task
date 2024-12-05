from pydantic import BaseModel


class UserBase(BaseModel):
    name: str


class UserResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class MovieBase(BaseModel):
    title: str


class MovieResponse(BaseModel):
    id: int
    title: str

    class Config:
        from_attributes = True
