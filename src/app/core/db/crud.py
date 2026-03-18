from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.core.db.models.links import Link

async def insert_short_link(session: AsyncSession, original_url: str, short_link: str) -> Link:
    new_link = Link(original_url=original_url, short_id=short_link)
    session.add(new_link)
    await session.commit()
    await session.refresh(new_link)
    return new_link

async def get_original_url(session: AsyncSession, short_link: str) -> Link | None:
    stmt = select(Link).where(Link.short_id == short_link)
    result = await session.execute(stmt)
    return result.scalars().one_or_none()

async def increment_clicks(session: AsyncSession, short_link: str) -> None:
    await session.execute(
        update(Link)
        .where(Link.short_id == short_link)
        .values(count=Link.count + 1)
    )
    await session.commit()