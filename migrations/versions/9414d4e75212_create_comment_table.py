"""create comment table

Revision ID: 9414d4e75212
Revises: 96397efe7376
Create Date: 2023-06-19 20:18:28.992493

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9414d4e75212'
down_revision = '96397efe7376'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('from_user_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['from_user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comment')
    # ### end Alembic commands ###
