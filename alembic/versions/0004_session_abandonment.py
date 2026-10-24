"""Allow explicit abandonment of incomplete sessions.

Revision ID: 0004_session_abandonment
Revises: 0003_random_colors_and_trial_counts
Create Date: 2026-10-23
"""

from alembic import op

revision = "0004_session_abandonment"
down_revision = "0003_random_colors_and_trial_counts"
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table("survey_sessions") as batch_op:
        batch_op.create_check_constraint(
            "ck_sessions_status",
            "status IN ('in_progress', 'completed', 'abandoned')",
        )


def downgrade() -> None:
    with op.batch_alter_table("survey_sessions") as batch_op:
        batch_op.drop_constraint("ck_sessions_status", type_="check")
