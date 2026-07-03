"""create users table

Revision ID: af3c0a88d163
Revises: c6f3e19f730f
Create Date: 2026-07-03 19:11:23.409370

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'af3c0a88d163'
down_revision: Union[str, Sequence[str], None] = 'c6f3e19f730f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
