"""add content column to posts table

Revision ID: b7dc8dd0934a
Revises: 2a3f1ebcd0a4
Create Date: 2022-12-22 00:28:14.266462

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b7dc8dd0934a'
down_revision = '2a3f1ebcd0a4'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',  sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
