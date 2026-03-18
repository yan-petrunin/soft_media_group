from pydantic import BaseModel, Field

class ShortenBody(BaseModel):
    link: str = Field(description="Ссылка, которую нужно сократить")

class ShortenResponse(BaseModel):
    short_link: str = Field(description="Сокращенная ссылка")