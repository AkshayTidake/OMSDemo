"""create refresh token table

Revision ID: 8f0bf9748404
Revises: af3c0a88d163
Create Date: 2026-07-05 00:26:28.314771

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8f0bf9748404'
down_revision: Union[str, Sequence[str], None] = 'af3c0a88d163'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
