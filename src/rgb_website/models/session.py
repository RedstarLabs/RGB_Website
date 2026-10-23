from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import Enum, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from rgb_website.database.base import Base
from rgb_website.experiment import PALETTE_VERSION

if TYPE_CHECKING:
    from rgb_website.models.response import Response
    from rgb_website.models.session_color import SessionColor


class SurveySession(Base):
    __tablename__ = "survey_sessions"

    id: Mapped[str] = mapped_column(String(128), primary_key=True)
    experiment_version: Mapped[str] = mapped_column(
        String(32),
        default=PALETTE_VERSION,
        nullable=False,
    )
    palette_version: Mapped[str] = mapped_column(
        String(32),
        default=PALETTE_VERSION,
        nullable=False,
    )
    status: Mapped[str] = mapped_column(
        Enum(
            "in_progress",
            "completed",
            name="survey_status",
            native_enum=False,
            length=11,
        ),
        default="in_progress",
        nullable=False,
    )

    responses: Mapped[list[Response]] = relationship(
        back_populates="session",
        cascade="all, delete-orphan",
    )
    colors: Mapped[list[SessionColor]] = relationship(
        back_populates="session",
        cascade="all, delete-orphan",
        order_by="SessionColor.position",
    )
