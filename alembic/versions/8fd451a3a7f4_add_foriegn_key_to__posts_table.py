"""add_foriegn_key_to _posts_table

Revision ID: 8fd451a3a7f4
Revises: 5d0be436bdca
Create Date: 2023-04-06 00:15:18.455636

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fd451a3a7f4'
down_revision = '5d0be436bdca'
branch_labels = None
depends_on = None


def upgrade() :
    op.add_column("posts",sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("post_users_fk",source_table="posts", referent_table="User",local_cols=['owner_id'],remote_cols=['id'], ondelete="CASCADE")


def downgrade():
    op.drop_constraint("post_users_fk", table_name="posts")
    op.drop_column("posts", "owner_id")
    
