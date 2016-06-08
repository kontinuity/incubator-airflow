"""Moved datetime to microseconds

Revision ID: 8aa568a05398
Revises: 2e82aab8ef20
Create Date: 2016-06-08 11:09:30.695700

"""

# revision identifiers, used by Alembic.
from sqlalchemy import DateTime

revision = '8aa568a05398'
down_revision = '2e82aab8ef20'
branch_labels = None
depends_on = None

from alembic import op
from sqlalchemy.dialects.mysql import DATETIME


def upgrade():
    with op.batch_alter_table("dag_run") as batch_op:
        batch_op.alter_column('execution_date',
                              existing_type=DateTime,
                              type_=DATETIME(fsp=6))
        batch_op.alter_column('start_date',
                              existing_type=DateTime,
                              type_=DATETIME(fsp=6))
        batch_op.alter_column('end_date',
                              existing_type=DateTime,
                              type_=DATETIME(fsp=6))

    with op.batch_alter_table("task_instance") as batch_op:
        batch_op.alter_column('execution_date',
                              existing_type=DateTime,
                              type_=DATETIME(fsp=6))
        batch_op.alter_column('start_date',
                              existing_type=DateTime,
                              type_=DATETIME(fsp=6))
        batch_op.alter_column('end_date',
                              existing_type=DateTime,
                              type_=DATETIME(fsp=6))

    with op.batch_alter_table("dag") as batch_op:
        batch_op.alter_column('last_scheduler_run',
                              existing_type=DateTime,
                              type_=DATETIME(fsp=6))
        batch_op.alter_column('last_pickled',
                              existing_type=DateTime,
                              type_=DATETIME(fsp=6))
        batch_op.alter_column('last_expired',
                              existing_type=DateTime,
                              type_=DATETIME(fsp=6))


def downgrade():
    pass
