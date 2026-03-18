from typing import Annotated
from src.app.core.schema.stats import StatsResponse
from src.app.settings.settings import config
from fastapi import APIRouter, Depends, Path, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from src.app.core.db.crud import get_original_url

stats = APIRouter()


@stats.get("/stats/{short_id}")
async def get_click_stat(
    short_id: Annotated[str, Path()],
    db_session: Annotated[AsyncSession, Depends(config.db_helper.session_dependency)],
):
    link = await get_original_url(db_session, short_id)
    if not link:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Link not found")
    return StatsResponse(count=link.count)