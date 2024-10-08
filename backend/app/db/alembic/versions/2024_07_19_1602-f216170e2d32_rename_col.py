"""rename col

Revision ID: f216170e2d32
Revises: 
Create Date: 2024-07-19 16:02:08.347933

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'f216170e2d32'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('alternatives', sa.Column('alternative_obj', sa.PickleType(), nullable=True))
    op.drop_column('alternatives', 'values')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('alternatives', sa.Column('values', postgresql.BYTEA(), autoincrement=False, nullable=True))
    op.drop_column('alternatives', 'alternative_obj')
    # ### end Alembic commands ###
