"""add_last_few_columns_to posts

Revision ID: 328f140eb115
Revises: 8fd451a3a7f4
Create Date: 2023-04-06 11:06:46.225572

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '328f140eb115'
down_revision = '8fd451a3a7f4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("published", sa.Boolean(),  server_default="True",nullable=False),
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True),server_default=sa.text("now()") ,nullable=False)))

def downgrade():
    op.drop_column("posts","published")
    op.drop_column("posts","created_at")
