"""add some column in posts table

Revision ID: 66d17a653344
Revises: 4c3c644158e3
Create Date: 2022-12-22 11:28:53.266996

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66d17a653344'
down_revision = '4c3c644158e3'
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
