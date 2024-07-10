"""init_db

Revision ID: 194475990c1b
Revises:
Create Date: 2024-07-10 01:09:55.859164

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '194475990c1b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categorias',
    sa.Column('pk_id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.PrimaryKeyConstraint('pk_id'),
    sa.UniqueConstraint('nome')
    )
    op.create_table('centros_treinamento',
    sa.Column('pk_id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('endereco', sa.String(length=60), nullable=False),
    sa.Column('proprietario', sa.String(length=30), nullable=False),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.PrimaryKeyConstraint('pk_id'),
    sa.UniqueConstraint('nome')
    )
    op.create_table('atletas',
    sa.Column('pk_id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('cpf', sa.String(length=11), nullable=False),
    sa.Column('idade', sa.Integer(), nullable=False),
    sa.Column('peso', sa.Float(), nullable=False),
    sa.Column('altura', sa.Float(), nullable=False),
    sa.Column('sexo', sa.String(length=1), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('categoria_id', sa.Integer(), nullable=False),
    sa.Column('centro_treinamento_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.ForeignKeyConstraint(['categoria_id'], ['categorias.pk_id'], ),
    sa.ForeignKeyConstraint(['centro_treinamento_id'], ['centros_treinamento.pk_id'], ),
    sa.PrimaryKeyConstraint('pk_id'),
    sa.UniqueConstraint('cpf')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('atletas')
    op.drop_table('centros_treinamento')
    op.drop_table('categorias')
    # ### end Alembic commands ###
