"""seed

Revision ID: 2ab12fbd5ff4
Revises: 6b0fab9d4234
Create Date: 2024-10-29 22:30:30.331196

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel.sql.sqltypes

import sgerbwd.models

# revision identifiers, used by Alembic.
revision: str = '2ab12fbd5ff4'
down_revision: Union[str, None] = '6b0fab9d4234'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    users_table = sgerbwd.models.User.metadata.tables['users']
    op.bulk_insert(table=users_table, rows=[
        {'name': 'John1', 'surname': 'Smith1'},
        {'name': 'John2', 'surname': 'Smith2'},
        {'name': 'John3', 'surname': 'Smith3'},
    ])


def downgrade() -> None:
    op.execute('delete from users')
