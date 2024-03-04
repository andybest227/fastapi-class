"""Add pulished column to posts table

Revision ID: 30d5cc5a4ce3
Revises: be12bcfaef1c
Create Date: 2024-03-03 19:35:09.639184

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '30d5cc5a4ce3'
down_revision: Union[str, None] = 'be12bcfaef1c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable=False, server_default=sa.text('True')),
                  sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('NOW()'), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    pass
