from sqlalchemy import BigInteger, Column, String, sql

from utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'

    user_id = Column(BigInteger, primary_key=True, unique=True)
    first_name = Column(String(200))
    last_name = Column(String(200))
    username = Column(String(50))
    status = Column(String(30))
    native_language = Column(String(30), primary_key=True)
    language_to_learn = Column(String(30), primary_key=True)
    words = Column(String(200), primary_key=True)

    query: sql.select
