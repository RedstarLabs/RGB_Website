from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from rgb_website.database.base import Base

if TYPE_CHECKING:
    from rgb_website.models.session import SurveySession


class SessionColor(Base):
    __tablename__ = "session_colors"
    __table_args__ = (
        UniqueConstraint("session_id", "color_id"),
        UniqueConstraint("session_id", "position"),
        CheckConstraint("position BETWEEN 1 AND 15", name="ck_colors_position"),
        CheckConstraint("color_r BETWEEN 0 AND 255", name="ck_colors_color_r"),
        CheckConstraint("color_g BETWEEN 0 AND 255", name="ck_colors_color_g"),
        CheckConstraint("color_b BETWEEN 0 AND 255", name="ck_colors_color_b"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    session_id: Mapped[str] = mapped_column(
        String(128),
        ForeignKey("survey_sessions.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    color_id: Mapped[str] = mapped_column(String(32), nullable=False)
    position: Mapped[int] = mapped_column(Integer, nullable=False)
    color_r: Mapped[int] = mapped_column(Integer, nullable=False)
    color_g: Mapped[int] = mapped_column(Integer, nullable=False)
    color_b: Mapped[int] = mapped_column(Integer, nullable=False)

    session: Mapped[SurveySession] = relationship(back_populates="colors")
