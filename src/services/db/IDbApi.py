from abc import ABC, abstractmethod

from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker

from src.models.db_models.account import Account
from src.models.db_models.category import Category
from src.models.db_models.operation import Operation
from src.models.db_models.sub_categories import SubCategory
from src.models.db_models.user import User


class IDbApi(ABC):

    def __init__(self, engine: AsyncEngine, session: async_sessionmaker):
        self.engine = engine
        self.session = session

    @abstractmethod
    async def insert(self, data: User | Account | Category | SubCategory | Operation) -> None:
        ...

    @abstractmethod
    async def get_user_by_id(self, _id: int) -> dict:
        """
        Select user from db by id
        :param _id: user id to select
        :return: user in dict if existed, empty dict if user with id not exist
        """
        ...

    @abstractmethod
    async def get_account_by_id(self, _id: int) -> dict:
        ...

    @abstractmethod
    async def get_operation_by_id(self, _id: int) -> dict:
        ...

    @abstractmethod
    async def get_category_by_id(self, _id: int) -> dict:
        ...

    @abstractmethod
    async def get_sub_category_by_id(self, _id: int) -> dict:
        ...

    # @abstractmethod
    # async def delete_user_by_id(self, _id: int):
    #     ...
    #
    # @abstractmethod
    # async def update_user_by_id(
    #         self, _id: int,
    #         name: str | None = None,
    #         timezone: int | None = None
    # ):
    #     ...
    #
    # @abstractmethod
    # async def update_account(self):
    #     ...
    #
    # @abstractmethod
    # async def delete_account_by_id(self):
    #     ...
    #
    # @abstractmethod
    # async def delete_category_by_id(self, _id: int):
    #     ...
    #
    # @abstractmethod
    # async def update_category(self):
    #     ...
    #
    # @abstractmethod
    # async def delete_sub_category(self):
    #     ...
    #
    # @abstractmethod
    # async def update_sub_category(self):
    #     ...
    #
    # @abstractmethod
    # async def delete_operation(self):
    #     ...
    #
    # @abstractmethod
    # async def update_operation(self):
    #     ...
