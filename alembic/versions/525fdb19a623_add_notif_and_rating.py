"""add_notif_and_rating

Revision ID: 525fdb19a623
Revises: bfa670b98f9c
Create Date: 2021-05-25 18:48:07.597129

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '525fdb19a623'
down_revision = 'bfa670b98f9c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('daily_notification', sa.Boolean(), server_default=sa.text('1'), nullable=False))
    op.add_column('users', sa.Column('show_in_rating', sa.Boolean(), server_default=sa.text('1'), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'show_in_rating')
    op.drop_column('users', 'daily_notification')
    # ### end Alembic commands ###
