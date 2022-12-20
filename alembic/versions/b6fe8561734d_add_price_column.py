"""Add price column

Revision ID: b6fe8561734d
Revises: bbe5a3a03f03
Create Date: 2022-12-20 14:50:13.207782

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6fe8561734d'
down_revision = 'bbe5a3a03f03'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('cars', sa.Column('price', sa.Integer))


def downgrade() -> None:
    op.drop_column('cars', 'price')
