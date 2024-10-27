from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    user_id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    surname: str = Field(index=True)

    __tablename__ = 'users'  # pyright: ignore
