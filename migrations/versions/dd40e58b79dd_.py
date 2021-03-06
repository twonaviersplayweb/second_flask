"""empty message

Revision ID: dd40e58b79dd
Revises: 1f68a58dde9
Create Date: 2016-10-27 17:17:37.775000

"""

# revision identifiers, used by Alembic.
revision = 'dd40e58b79dd'
down_revision = '1f68a58dde9'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    ### end Alembic commands ###
