from sqlalchemy.orm import Mapped, mapped_column

from src.models.db_models.meta import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    timezone: Mapped[int]
