from sqlalchemy import exists, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import Language
from src.routers.languages.schemes import LanguageOutScheme


class LanguageRepo:
    @staticmethod
    async def exists(
            language_id: int,
            db_session: AsyncSession
    ) -> bool:
        result = await db_session.execute(
            select(exists().where(Language.id == language_id))
        )
        return result.scalar_one_or_none()

    @staticmethod
    async def get_list(
            db_session: AsyncSession
    ) -> list[LanguageOutScheme]:
        result = await db_session.execute(select(Language))
        return [
            LanguageOutScheme.model_validate(l) for l in result.scalars().all()
        ]

    @staticmethod
    async def get_by_id(
            language_id: int,
            db_session: AsyncSession
    ) -> Language | None:
        result = await db_session.execute(select(Language).filter_by(
            id=language_id
        ))
        return result.scalar_one_or_none()