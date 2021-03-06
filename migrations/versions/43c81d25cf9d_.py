"""empty message

Revision ID: 43c81d25cf9d
Revises: 10d71993e15e
Create Date: 2016-10-27 16:18:56.740000

"""

# revision identifiers, used by Alembic.
revision = '43c81d25cf9d'
down_revision = '10d71993e15e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.String(length=64), nullable=True))
    op.add_column('user', sa.Column('password_hash', sa.String(length=128), nullable=True))
    op.drop_column('user', 'country')
    op.create_index('ix_user_email', 'user', ['email'], unique=True)
    op.drop_index('ix_user_country', 'user')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_user_country', 'user', ['country'], unique=1)
    op.drop_index('ix_user_email', 'user')
    op.add_column('user', sa.Column('country', sa.VARCHAR(length=64), nullable=True))
    op.drop_column('user', 'password_hash')
    op.drop_column('user', 'email')
    ### end Alembic commands ###
