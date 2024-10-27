"""create schema

Revision ID: ec5ddda825ce
Revises:
Create Date: 2023-01-22 15:43:12.663404

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'ec5ddda825ce'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('user_id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(64), nullable=False),
        sa.Column('surname', sa.String(64), nullable=False),
        sqlite_autoincrement=True,
    )


def downgrade() -> None:
    op.drop_table('users')
