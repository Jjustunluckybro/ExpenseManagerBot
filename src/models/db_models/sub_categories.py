from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.models.db_models.meta import Base


class SubCategory(Base):
    __tablename__ = "sub_categories"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))
    name: Mapped[str]
    is_income: Mapped[bool] = mapped_column(default=True)
