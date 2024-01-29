from sqlalchemy import Column, String
from .base import BaseModel


class UserDB(BaseModel):
    __tablename__: str = "users"
    username = Column(String)
    password = Column(String)
    role = Column(String)
    salt = Column(String)
