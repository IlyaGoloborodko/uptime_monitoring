"""fix

Revision ID: 60a4d488816b
Revises: 9faf39ef8ee7
Create Date: 2025-03-09 19:16:24.592110

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '60a4d488816b'
down_revision: Union[str, None] = '9faf39ef8ee7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('requestconfig',
    sa.Column('url', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('method', sa.Enum('GET', 'POST', 'PUT', 'DELETE', name='httpmethod'), nullable=False),
    sa.Column('params', sa.JSON(), nullable=True),
    sa.Column('headers', sa.JSON(), nullable=True),
    sa.Column('timeout', sa.Integer(), nullable=False),
    sa.Column('max_retries', sa.Integer(), nullable=False),
    sa.Column('retry_interval', sa.Integer(), nullable=False),
    sa.Column('frequency', sa.Integer(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('requestconfig')
    # ### end Alembic commands ###
