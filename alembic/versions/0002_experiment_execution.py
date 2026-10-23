"""Add persisted experiment execution data.

Revision ID: 0002_experiment_execution
Revises: 0001_initial_schema
Create Date: 2026-10-23
"""

import sqlalchemy as sa

from alembic import op

revision = "0002_experiment_execution"
down_revision = "0001_initial_schema"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        "survey_sessions",
        sa.Column(
            "palette_version",
            sa.String(length=32),
            nullable=False,
            server_default="1.0",
        ),
    )
    op.add_column(
        "survey_sessions",
        sa.Column(
            "status",
            sa.String(length=11),
            nullable=False,
            server_default="in_progress",
        ),
    )
    op.create_table(
        "session_colors",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("session_id", sa.String(length=128), nullable=False),
        sa.Column("color_id", sa.String(length=32), nullable=False),
        sa.Column("position", sa.Integer(), nullable=False),
        sa.Column("color_r", sa.Integer(), nullable=False),
        sa.Column("color_g", sa.Integer(), nullable=False),
        sa.Column("color_b", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["session_id"], ["survey_sessions.id"], ondelete="CASCADE"
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("session_id", "color_id"),
        sa.UniqueConstraint("session_id", "position"),
    )
    op.create_index(
        "ix_session_colors_session_id",
        "session_colors",
        ["session_id"],
        unique=False,
    )
    with op.batch_alter_table("responses") as batch_op:
        batch_op.add_column(sa.Column("color_id", sa.String(length=32)))
        batch_op.create_unique_constraint(
            "uq_responses_session_color",
            ["session_id", "color_id"],
        )


def downgrade() -> None:
    with op.batch_alter_table("responses") as batch_op:
        batch_op.drop_constraint("uq_responses_session_color", type_="unique")
        batch_op.drop_column("color_id")
    op.drop_index("ix_session_colors_session_id", table_name="session_colors")
    op.drop_table("session_colors")
    op.drop_column("survey_sessions", "status")
    op.drop_column("survey_sessions", "palette_version")
