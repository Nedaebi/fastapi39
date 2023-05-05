"""add  content column to posts table

Revision ID: 2e60b35d6327
Revises: f7c5c4c286d8
Create Date: 2023-04-04 00:29:32.861331

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2e60b35d6327'
down_revision = 'f7c5c4c286d8'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts",sa.Column("content",sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_column("posts", "content")
