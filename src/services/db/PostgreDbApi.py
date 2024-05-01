from sqlalchemy import text

from src.models.db_models.account import Account
from src.models.db_models.category import Category
from src.models.db_models.operation import Operation
from src.models.db_models.sub_categories import SubCategory
from src.models.db_models.user import User
from src.services.db.IDbApi import IDbApi


class PostgresAPI(IDbApi):

    async def insert(self, data: User | Account | Category | SubCategory | Operation) -> None:
        async with self.session() as s:
            s.add(data)
            await s.commit()

    async def get_user_by_id(self, _id: int) -> dict:
        async with self.session() as s:
            query = text(f"SELECT * FROM users WHERE id = {_id}")
            res = await s.execute(query)
            res = res.mappings().all()
            return res[0] if len(res) == 1 else {}

    async def get_account_by_id(self, _id: int) -> dict:
        async with self.session() as s:
            query = text(f"SELECT * FROM accounts WHERE id = {_id}")
            res = await s.execute(query)
            res = res.mappings().all()
            return res[0] if len(res) == 1 else {}

    async def get_category_by_id(self, _id: int) -> dict:
        async with self.session() as s:
            query = text(f"SELECT * FROM categories WHERE id = {_id}")
            res = await s.execute(query)
            res = res.mappings().all()
            return res[0] if len(res) == 1 else {}

    async def get_sub_category_by_id(self, _id: int) -> dict:
        async with self.session() as s:
            query = text(f"SELECT * FROM categories WHERE id = {_id}")
            res = await s.execute(query)
            res = res.mappings().all()
            return res[0] if len(res) == 1 else {}

    async def get_operation_by_id(self, _id: int) -> dict:
        async with self.session() as s:
            query = text(f"SELECT * FROM operations WHERE id = {_id}")
            res = await s.execute(query)
            res = res.mappings().all()
            return res[0] if len(res) == 1 else {}


