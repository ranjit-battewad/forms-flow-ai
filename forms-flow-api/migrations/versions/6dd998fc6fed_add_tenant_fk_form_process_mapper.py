"""add_tenant_fk_form_process_mapper

Revision ID: 6dd998fc6fed
Revises: 07591848eb83
Create Date: 2022-05-11 12:46:32.944166

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '6dd998fc6fed'
down_revision = '07591848eb83'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('_form_version_uc', 'form_process_mapper', type_='unique')
    op.create_unique_constraint('_form_version_uc', 'form_process_mapper', ['form_id', 'version', 'tenant'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('_form_version_uc', 'form_process_mapper', type_='unique')
    op.create_unique_constraint('_form_version_uc', 'form_process_mapper', ['form_id', 'version'])
    # ### end Alembic commands ###
