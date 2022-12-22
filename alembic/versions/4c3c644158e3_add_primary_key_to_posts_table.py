"""add primary-key to posts table

Revision ID: 4c3c644158e3
Revises: 44a9717e0e51
Create Date: 2022-12-22 10:36:06.168545

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c3c644158e3'
down_revision = '44a9717e0e51'
branch_labels = None
depends_on = None


def upgrade():
    
    op.create_primary_key('posts_pkey', table_name="posts", columns=['id'])
    pass


def downgrade():
    op.drop_constraint('posts_pkey', table_name="posts")
    pass
