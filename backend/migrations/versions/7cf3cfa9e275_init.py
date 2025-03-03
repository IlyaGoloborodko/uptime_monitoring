"""init

Revision ID: 7cf3cfa9e275
Revises: 
Create Date: 2025-03-03 21:10:36.124119

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '7cf3cfa9e275'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('requestconfig',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('url', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('method', sa.Enum('GET', 'POST', 'PUT', 'DELETE', name='httpmethod'), nullable=False),
    sa.Column('params', sa.JSON(), nullable=True),
    sa.Column('body', sa.JSON(), nullable=True),
    sa.Column('headers', sa.JSON(), nullable=True),
    sa.Column('content_type', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('frequency', sa.Integer(), nullable=False),
    sa.Column('timeout', sa.Integer(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('max_retries', sa.Integer(), nullable=False),
    sa.Column('retry_interval', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('requestconfig')
    # ### end Alembic commands ###
