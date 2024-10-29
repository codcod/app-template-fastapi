from sqlmodel import Field, SQLModel

NAMING_CONVENTION = {
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s',
}

metadata = SQLModel.metadata
metadata.naming_convention = NAMING_CONVENTION


class User(SQLModel, table=True):
    user_id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    surname: str = Field(index=True)

    __tablename__ = 'users'  # pyright: ignore
