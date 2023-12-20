"""Init

Revision ID: 8abc460c33af
Revises: 
Create Date: 2023-12-14 14:58:17.586096

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8abc460c33af'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contacts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=50), nullable=True),
    sa.Column('lastname', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('phone', sa.String(length=15), nullable=False),
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.Column('additional_info', sa.String(length=150), nullable=True),
    sa.Column('is_favorite', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_contacts_email'), 'contacts', ['email'], unique=True)
    op.create_index(op.f('ix_contacts_firstname'), 'contacts', ['firstname'], unique=False)
    op.create_index(op.f('ix_contacts_lastname'), 'contacts', ['lastname'], unique=False)
    op.create_index(op.f('ix_contacts_phone'), 'contacts', ['phone'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_contacts_phone'), table_name='contacts')
    op.drop_index(op.f('ix_contacts_lastname'), table_name='contacts')
    op.drop_index(op.f('ix_contacts_firstname'), table_name='contacts')
    op.drop_index(op.f('ix_contacts_email'), table_name='contacts')
    op.drop_table('contacts')
    # ### end Alembic commands ###
