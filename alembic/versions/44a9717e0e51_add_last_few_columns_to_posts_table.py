"""add last few columns to posts table

Revision ID: 44a9717e0e51
Revises: a3e5f6db386d
Create Date: 2022-12-22 10:09:17.460813

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44a9717e0e51'
down_revision = 'a3e5f6db386d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(),server_default='True', nullable=False))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False,server_default=sa.text('NOW()')),)
    pass

def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
