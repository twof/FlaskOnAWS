"""empty message

Revision ID: 22849ef64d33
Revises: 
Create Date: 2018-11-23 17:08:44.626628

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22849ef64d33'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('global_todo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('global_todo')
    # ### end Alembic commands ###