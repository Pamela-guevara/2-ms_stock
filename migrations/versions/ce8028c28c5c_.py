"""empty message

Revision ID: ce8028c28c5c
Revises: 1fd204f8ac4d
Create Date: 2024-10-27 20:04:22.110472

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'ce8028c28c5c'
down_revision = '1fd204f8ac4d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('stocks', schema=None) as batch_op:
        batch_op.alter_column('transaction_date',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.DateTime(timezone=True),
               existing_nullable=True,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))
        batch_op.alter_column('active',
               existing_type=sa.BOOLEAN(),
               nullable=True,
               existing_server_default=sa.text('true'))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('stocks', schema=None) as batch_op:
        batch_op.alter_column('active',
               existing_type=sa.BOOLEAN(),
               nullable=False,
               existing_server_default=sa.text('true'))
        batch_op.alter_column('transaction_date',
               existing_type=sa.DateTime(timezone=True),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=True,
               existing_server_default=sa.text('CURRENT_TIMESTAMP'))

    # ### end Alembic commands ###
