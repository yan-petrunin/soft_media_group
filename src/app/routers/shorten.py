from typing import Annotated
from src.app.core.short_link import generate_short_id
from src.app.settings.settings import config
from fastapi import APIRouter, Body, Depends, Path, HTTPException, status
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession
from src.app.core.schema.shorten import ShortenBody, ShortenResponse
from src.app.core.db.crud import insert_short_link, get_original_url, increment_clicks
shorten = APIRouter()


@shorten.post("/shorten")
async def create_short_link(
    body: Annotated[ShortenBody, Body()],
    db_session: Annotated[AsyncSession, Depends(config.db_helper.session_dependency)],
):
    short_id = generate_short_id()
    if not (body.link.startswith("http://") or body.link.startswith("https://")):
        body.link = "https://" + body.link

    new_link = await insert_short_link(db_session, body.link, short_id)
    return ShortenResponse(short_link=new_link.short_id)

@shorten.get("/{short_id}")
async def get_link(
    short_id: Annotated[str, Path()],
    db_session: Annotated[AsyncSession, Depends(config.db_helper.session_dependency)],
):
    link = await get_original_url(db_session, short_id)
    if not link:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Original link not found")
    await increment_clicks(db_session, short_id)
    return RedirectResponse(url=str(link.original_url))