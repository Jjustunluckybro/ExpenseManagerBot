from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.models.db_models.meta import Base


class Operation(Base):
    __tablename__ = "operations"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"))
    amount: Mapped[float]
    dt: Mapped[datetime]
    category: Mapped[str] = mapped_column(ForeignKey("categories.id"))
    sub_category: Mapped[str | None] = mapped_column(ForeignKey("sub_categories.id"))
