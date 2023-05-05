"""create _User_table

Revision ID: 5d0be436bdca
Revises: 2e60b35d6327
Create Date: 2023-04-05 23:23:27.113357

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d0be436bdca'
down_revision = '2e60b35d6327'
branch_labels = None
depends_on = None


def upgrade() :
     op.create_table('User', sa.Column("id", sa.Integer(), nullable=False),
    sa.Column("email", sa.String(), nullable=False), sa.Column("password", sa.String(), nullable=False), 
    sa.Column("created_at", sa.TIMESTAMP(timezone=True),server_default=sa.text("now()") ,nullable=False),
    sa.PrimaryKeyConstraint('id'), 
    sa.UniqueConstraint("email")
    )
  


def downgrade():
    op.drop_table("User")
