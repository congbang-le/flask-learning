"""create cars table

Revision ID: bbe5a3a03f03
Revises: 
Create Date: 2022-12-20 14:41:58.252198

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bbe5a3a03f03'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'cars',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('brand', sa.Unicode(200)),
        sa.Column('type', sa.Unicode(200)),
        sa.Column('seats', sa.Integer),
    )



def downgrade() -> None:
    op.drop_table('cars')
