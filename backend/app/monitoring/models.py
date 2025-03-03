from typing import Optional

from sqlmodel import Field, SQLModel


class RequestConfig(SQLModel, table=True):
    id: int | None = Field(primary_key=True)
    # FK
    url: str
    method: str
    params: Optional[str] = Field(default=None, nullable=True)

