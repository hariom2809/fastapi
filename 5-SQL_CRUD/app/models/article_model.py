from app.database.db import Base
from sqlalchemy import Column, Integer, String, Text

class Article(Base):
    __tablename__ = "Article"

    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    content = Column(Text)
    author = Column(String(50))
    