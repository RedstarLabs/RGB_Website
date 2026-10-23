"""Add random RGB snapshots, configurable trial counts, and timestamps.

Revision ID: 0003_random_colors_and_trial_counts
Revises: 0002_experiment_execution
Create Date: 2026-10-23
"""

import sqlalchemy as sa

from alembic import op

revision = "0003_random_colors_and_trial_counts"
down_revision = "0002_experiment_execution"
branch_labels = None
depends_on = None


RESPONSE_CHECKS = (
    sa.CheckConstraint(
        "trial_number BETWEEN 1 AND 15",
        name="ck_responses_trial_number",
    ),
    sa.CheckConstraint("color_r BETWEEN 0 AND 255", name="ck_responses_color_r"),
    sa.CheckConstraint("color_g BETWEEN 0 AND 255", name="ck_responses_color_g"),
    sa.CheckConstraint("color_b BETWEEN 0 AND 255", name="ck_responses_color_b"),
    sa.CheckConstraint(
        "color_order BETWEEN 1 AND 15",
        name="ck_responses_color_order",
    ),
)


def upgrade() -> None:
    op.add_column(
        "survey_sessions",
        sa.Column(
            "trial_count",
            sa.Integer(),
            nullable=False,
            server_default="10",
        ),
    )
    with op.batch_alter_table("survey_sessions") as batch_op:
        batch_op.create_check_constraint(
            "ck_sessions_trial_count",
            "trial_count IN (10, 15)",
        )
    with op.batch_alter_table(
        "responses",
        table_args=list(RESPONSE_CHECKS),
    ) as batch_op:
        batch_op.add_column(
            sa.Column("response_timestamp", sa.DateTime(timezone=True), nullable=True)
        )
    with op.batch_alter_table("session_colors") as batch_op:
        batch_op.create_check_constraint(
            "ck_colors_position",
            "position BETWEEN 1 AND 15",
        )
        batch_op.create_check_constraint(
            "ck_colors_color_r", "color_r BETWEEN 0 AND 255"
        )
        batch_op.create_check_constraint(
            "ck_colors_color_g", "color_g BETWEEN 0 AND 255"
        )
        batch_op.create_check_constraint(
            "ck_colors_color_b", "color_b BETWEEN 0 AND 255"
        )


def downgrade() -> None:
    with op.batch_alter_table("session_colors") as batch_op:
        for name in (
            "ck_colors_position",
            "ck_colors_color_r",
            "ck_colors_color_g",
            "ck_colors_color_b",
        ):
            batch_op.drop_constraint(name, type_="check")
    with op.batch_alter_table("responses") as batch_op:
        batch_op.drop_column("response_timestamp")
    with op.batch_alter_table("survey_sessions") as batch_op:
        batch_op.drop_constraint("ck_sessions_trial_count", type_="check")
    op.drop_column("survey_sessions", "trial_count")
