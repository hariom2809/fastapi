from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app.core.config import settings

engine = create_engine(url=settings.DB_URL)

SessionLocal = sessionmaker(bind=engine)

Base =  declarative_base()