from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    ForeignKey,
    Integer,
    String,
    UniqueConstraint,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from rgb_website.database.base import Base

if TYPE_CHECKING:
    from rgb_website.models.session import SurveySession


class Response(Base):
    __tablename__ = "responses"
    __table_args__ = (
        UniqueConstraint("session_id", "trial_number"),
        UniqueConstraint("session_id", "color_id"),
        CheckConstraint(
            "trial_number BETWEEN 1 AND 15",
            name="ck_responses_trial_number",
        ),
        CheckConstraint("color_r BETWEEN 0 AND 255", name="ck_responses_color_r"),
        CheckConstraint("color_g BETWEEN 0 AND 255", name="ck_responses_color_g"),
        CheckConstraint("color_b BETWEEN 0 AND 255", name="ck_responses_color_b"),
        CheckConstraint(
            "color_order BETWEEN 1 AND 15",
            name="ck_responses_color_order",
        ),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    session_id: Mapped[str] = mapped_column(
        String(128),
        ForeignKey("survey_sessions.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    color_id: Mapped[str] = mapped_column(String(32), nullable=False)
    trial_number: Mapped[int] = mapped_column(Integer, nullable=False)
    color_r: Mapped[int] = mapped_column(Integer, nullable=False)
    color_g: Mapped[int] = mapped_column(Integer, nullable=False)
    color_b: Mapped[int] = mapped_column(Integer, nullable=False)
    emotion: Mapped[str] = mapped_column(String(64), nullable=False)
    color_order: Mapped[int] = mapped_column(Integer, nullable=False)
    experiment_version: Mapped[str] = mapped_column(String(32), nullable=False)
    response_timestamp: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    session: Mapped[SurveySession] = relationship(back_populates="responses")
