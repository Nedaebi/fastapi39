"""create posts table

Revision ID: f7c5c4c286d8
Revises: 
Create Date: 2023-04-01 20:47:28.078838

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7c5c4c286d8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',sa.Column('id',sa.Integer(),  primary_key=True), sa.Column('title', sa.String()))


def downgrade():
    op.drop_table('posts')