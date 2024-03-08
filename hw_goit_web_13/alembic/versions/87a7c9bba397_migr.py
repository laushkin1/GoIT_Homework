"""migr

Revision ID: 87a7c9bba397
Revises: 44560b35315e
Create Date: 2023-09-20 15:59:00.881337

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "87a7c9bba397"
down_revision: Union[str, None] = "44560b35315e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
