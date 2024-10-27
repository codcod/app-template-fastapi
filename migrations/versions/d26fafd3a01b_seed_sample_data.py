"""seed sample data

Revision ID: d26fafd3a01b
Revises: ec5ddda825ce
Create Date: 2023-01-22 15:43:34.071949

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = 'd26fafd3a01b'
down_revision = 'ec5ddda825ce'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("insert into users(name, surname) values('Jan1', 'Kowalski')")
    op.execute("insert into users(name, surname) values('Jan2', 'Kowalski')")
    op.execute("insert into users(name, surname) values('Jan3', 'Kowalski')")


def downgrade() -> None:
    op.execute('delete from users')
