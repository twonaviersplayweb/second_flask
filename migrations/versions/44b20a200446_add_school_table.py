"""add School table

Revision ID: 44b20a200446
Revises: 4ca3be6af9ed
Create Date: 2016-10-26 17:09:41.146000

"""

# revision identifiers, used by Alembic.
revision = '44b20a200446'
down_revision = '4ca3be6af9ed'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('school',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('school')
    ### end Alembic commands ###
