import asyncio

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.services.db.IDbApi import IDbApi
from src.services.db.PostgreDbApi import PostgresAPI
from src.config import CONFIG


async def prepare_db() -> IDbApi:
    db_engine = create_async_engine(
        url=CONFIG.db_url,
        echo=True
    )
    session_factory = async_sessionmaker(db_engine)
    db = PostgresAPI(db_engine, session_factory)
    return db


async def main() -> None:
    db = await prepare_db()


if __name__ == "__main__":
    asyncio.run(main())
