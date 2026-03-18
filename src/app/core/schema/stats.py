from pydantic import BaseModel, Field

class StatsResponse(BaseModel):
    count: int = Field(description="Количество переходов")