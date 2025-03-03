from sqlmodel import create_engine, SQLModel

from backend.app.models import *


from backend.app.core import settings

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
