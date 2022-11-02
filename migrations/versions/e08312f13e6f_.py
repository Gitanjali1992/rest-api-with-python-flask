"""empty message

Revision ID: e08312f13e6f
Revises: 76f313e7a8c9
Create Date: 2022-11-02 05:08:42.786679

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e08312f13e6f'
down_revision = '76f313e7a8c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(), nullable=False))
    op.create_unique_constraint("email", 'users', ['email'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("email", 'users', type_='unique')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
