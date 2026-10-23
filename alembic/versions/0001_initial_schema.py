"""Create initial survey schema.

Revision ID: 0001_initial_schema
Revises:
Create Date: 2026-10-23
"""

import sqlalchemy as sa

from alembic import op

revision = "0001_initial_schema"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "survey_sessions",
        sa.Column("id", sa.String(length=128), nullable=False),
        sa.Column("experiment_version", sa.String(length=32), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "responses",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("session_id", sa.String(length=128), nullable=False),
        sa.Column("trial_number", sa.Integer(), nullable=False),
        sa.Column("color_r", sa.Integer(), nullable=False),
        sa.Column("color_g", sa.Integer(), nullable=False),
        sa.Column("color_b", sa.Integer(), nullable=False),
        sa.Column("emotion", sa.String(length=64), nullable=False),
        sa.Column("color_order", sa.Integer(), nullable=False),
        sa.Column("experiment_version", sa.String(length=32), nullable=False),
        sa.CheckConstraint("trial_number BETWEEN 1 AND 10"),
        sa.CheckConstraint("color_r BETWEEN 0 AND 255"),
        sa.CheckConstraint("color_g BETWEEN 0 AND 255"),
        sa.CheckConstraint("color_b BETWEEN 0 AND 255"),
        sa.CheckConstraint("color_order BETWEEN 1 AND 10"),
        sa.ForeignKeyConstraint(
            ["session_id"],
            ["survey_sessions.id"],
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("session_id", "trial_number"),
    )
    op.create_index(
        "ix_responses_session_id",
        "responses",
        ["session_id"],
        unique=False,
    )


def downgrade() -> None:
    op.drop_index("ix_responses_session_id", table_name="responses")
    op.drop_table("responses")
    op.drop_table("survey_sessions")
