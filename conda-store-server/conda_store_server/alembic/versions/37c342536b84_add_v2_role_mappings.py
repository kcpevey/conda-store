"""add v2 role mappings

Revision ID: 37c342536b84
Revises: b387747ca9b7
Create Date: 2023-10-29 21:32:01.560843

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "37c342536b84"
down_revision = "b387747ca9b7"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "namespace_role_mapping_v2",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("namespace_id", sa.Integer(), nullable=False),
        sa.Column("other_namespace_id", sa.Integer(), nullable=False),
        sa.Column("role", sa.Unicode(length=255), nullable=False),
        sa.ForeignKeyConstraint(
            ["namespace_id"],
            ["namespace.id"],
        ),
        sa.ForeignKeyConstraint(
            ["other_namespace_id"],
            ["namespace.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("namespace_id", "other_namespace_id", name="_uc"),
    )


def downgrade():
    op.drop_table("namespace_role_mapping_v2")
