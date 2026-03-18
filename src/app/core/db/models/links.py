from src.app.core.db.models.base import Base
from sqlalchemy.orm import MappedColumn, mapped_column
from sqlalchemy import BigInteger, Text, String, DateTime, func

class Link(Base):
    __tablename__ = "links"

    id: MappedColumn[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    original_url: MappedColumn[str] = mapped_column(Text, nullable=False)
    short_id: MappedColumn[str] = mapped_column(String(10), nullable=False, unique=True)
    count: MappedColumn[int] = mapped_column(BigInteger, nullable=False, default=0)
    created_at: MappedColumn[int] = mapped_column(DateTime, nullable=False, default=func.now())