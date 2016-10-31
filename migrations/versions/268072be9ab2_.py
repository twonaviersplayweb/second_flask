"""empty message

Revision ID: 268072be9ab2
Revises: 43c81d25cf9d
Create Date: 2016-10-27 16:31:13.218000

"""

# revision identifiers, used by Alembic.
revision = '268072be9ab2'
down_revision = '43c81d25cf9d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'country')
    op.drop_column('user', 'password_hash')
    op.create_index('ix_user_email', 'user', ['email'], unique=True)
    op.drop_index('ix_user_country', 'user')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_user_country', 'user', ['country'], unique=1)
    op.drop_index('ix_user_email', 'user')
    op.add_column('user', sa.Column('password_hash', sa.VARCHAR(length=128), nullable=True))
    op.add_column('user', sa.Column('country', sa.VARCHAR(length=64), nullable=True))
    ### end Alembic commands ###
