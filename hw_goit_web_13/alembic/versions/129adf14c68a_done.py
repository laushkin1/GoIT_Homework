"""Done

Revision ID: 129adf14c68a
Revises: 87a7c9bba397
Create Date: 2023-09-20 16:00:57.705756

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "129adf14c68a"
down_revision: Union[str, None] = "87a7c9bba397"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
