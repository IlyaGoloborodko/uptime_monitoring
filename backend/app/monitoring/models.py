from sqlmodel import Field, SQLModel


class RequestConfig(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    # FK
    url: str
    params: str
    method: str = Field(default=None)
