"""Add created at column to posts table

Revision ID: ad499fe55275
Revises: 7c574c06a548
Create Date: 2024-03-03 21:39:05.501510

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ad499fe55275'
down_revision: Union[str, None] = '7c574c06a548'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()'), nullable=False))
  
    pass


def downgrade() -> None:
    op.drop_column('posts', 'created_at')
    pass
