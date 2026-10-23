from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from rgb_website.database.base import Base

if TYPE_CHECKING:
    from rgb_website.models.session import SurveySession


class Response(Base):
    __tablename__ = "responses"
    __table_args__ = (
        UniqueConstraint("session_id", "trial_number"),
        CheckConstraint("trial_number BETWEEN 1 AND 10"),
        CheckConstraint("color_r BETWEEN 0 AND 255"),
        CheckConstraint("color_g BETWEEN 0 AND 255"),
        CheckConstraint("color_b BETWEEN 0 AND 255"),
        CheckConstraint("color_order BETWEEN 1 AND 10"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    session_id: Mapped[str] = mapped_column(
        String(128),
        ForeignKey("survey_sessions.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    trial_number: Mapped[int] = mapped_column(Integer, nullable=False)
    color_r: Mapped[int] = mapped_column(Integer, nullable=False)
    color_g: Mapped[int] = mapped_column(Integer, nullable=False)
    color_b: Mapped[int] = mapped_column(Integer, nullable=False)
    emotion: Mapped[str] = mapped_column(String(64), nullable=False)
    color_order: Mapped[int] = mapped_column(Integer, nullable=False)
    experiment_version: Mapped[str] = mapped_column(String(32), nullable=False)

    session: Mapped[SurveySession] = relationship(back_populates="responses")
