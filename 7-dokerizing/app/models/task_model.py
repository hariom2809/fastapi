from uuid import uuid7, UUID
from sqlalchemy import UUID as sUUID
from sqlalchemy import String, Text, Date
from sqlalchemy.orm import Mapped, mapped_column
from datetime import date
from app.db.databse import Base

class Task(Base):
    __tablename__ = "tasks"

    id:             Mapped[UUID]        = mapped_column(sUUID, primary_key=True, index=True, default=uuid7)
    title:          Mapped[str]         = mapped_column(String(50), nullable=False)
    description:    Mapped[str]         = mapped_column(Text, nullable=True)
    created_at:     Mapped[date]        = mapped_column(Date, default=date.today, nullable=False)
    completed_at:   Mapped[date | None] = mapped_column(Date, nullable=True)
