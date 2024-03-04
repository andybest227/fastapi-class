"""Create posts table

Revision ID: be12bcfaef1c
Revises: 
Create Date: 2024-03-03 19:20:10.614182

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'be12bcfaef1c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts', 
                    sa.Column('id', sa.Integer(), primary_key=True, nullable=False), 
                    sa.Column('title', sa.String(), nullable=False), 
                    sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
