from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from rgb_website.database.base import Base

if TYPE_CHECKING:
    from rgb_website.models.response import Response


class SurveySession(Base):
    __tablename__ = "survey_sessions"

    id: Mapped[str] = mapped_column(String(128), primary_key=True)
    experiment_version: Mapped[str] = mapped_column(String(32), nullable=False)

    responses: Mapped[list[Response]] = relationship(
        back_populates="session",
        cascade="all, delete-orphan",
    )
