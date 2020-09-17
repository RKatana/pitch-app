"""removing some columns

Revision ID: 535ecccca644
Revises: 8ac3f3913194
Create Date: 2018-06-25 15:01:54.482732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '535ecccca644'
down_revision = '8ac3f3913194'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('comments_pitch_id_fkey', 'comments', type_='foreignkey')
    op.drop_column('comments', 'pitch_id')
    op.drop_column('pitches', 'upvotes')
    op.drop_column('pitches', 'downvotes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('downvotes', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('pitches', sa.Column('upvotes', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('comments', sa.Column('pitch_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('comments_pitch_id_fkey', 'comments', 'pitches', ['pitch_id'], ['id'])
    # ### end Alembic commands ###
