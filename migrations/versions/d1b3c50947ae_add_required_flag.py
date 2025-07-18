"""add required flag

Revision ID: d1b3c50947ae
Revises: de6c9891ffab
Create Date: 2025-07-15 11:37:34.445373

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1b3c50947ae'
down_revision = 'de6c9891ffab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('questions', schema=None) as batch_op:
        batch_op.add_column(
            sa.Column('is_required', sa.Boolean(), nullable=False, server_default=sa.true())
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('questions', schema=None) as batch_op:
        batch_op.drop_column('is_required')

    # ### end Alembic commands ###
