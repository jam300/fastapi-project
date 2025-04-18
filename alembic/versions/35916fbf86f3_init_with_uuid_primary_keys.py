"""init with uuid primary keys

Revision ID: 35916fbf86f3
Revises: 
Create Date: 2025-04-09 20:10:24.058462

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '35916fbf86f3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('uuid', sa.String(length=36), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('uuid'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_table('posts',
    sa.Column('uuid', sa.String(length=36), nullable=False),
    sa.Column('title', sa.String(length=150), nullable=False),
    sa.Column('content', sa.String(length=2000), nullable=False),
    sa.Column('published', sa.Boolean(), server_default='TRUE', nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('GETDATE()'), nullable=False),
    sa.Column('owner_uuid', sa.String(length=36), nullable=False),
    sa.ForeignKeyConstraint(['owner_uuid'], ['users.uuid'], name='fk_posts_owner_uuid', ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('uuid'),
    sa.UniqueConstraint('uuid')
    )
    op.create_index(op.f('ix_posts_owner_uuid'), 'posts', ['owner_uuid'], unique=False)
    op.create_table('votes',
    sa.Column('user_uuid', sa.String(length=36), nullable=False),
    sa.Column('post_uuid', sa.String(length=36), nullable=False),
    sa.ForeignKeyConstraint(['post_uuid'], ['posts.uuid'], name='fk_votes_post_uuid', ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_uuid'], ['users.uuid'], name='fk_votes_user_uuid', ondelete='NO ACTION'),
    sa.PrimaryKeyConstraint('user_uuid', 'post_uuid', name='pk_votes')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('votes')
    op.drop_index(op.f('ix_posts_owner_uuid'), table_name='posts')
    op.drop_table('posts')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
