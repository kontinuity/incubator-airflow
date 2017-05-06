"""convert to mediumblob

Revision ID: 6030dbb09e8c
Revises: 8aa568a05398
Create Date: 2017-05-06 20:52:24.133339

"""

# revision identifiers, used by Alembic.
from sqlalchemy.dialects.mysql.base import MSMediumBlob
from sqlalchemy.sql.sqltypes import PickleType

revision = '6030dbb09e8c'
down_revision = '8aa568a05398'
branch_labels = None
depends_on = None

from alembic import op


def upgrade():
    with op.batch_alter_table("celery_taskmeta") as batch_op:
        batch_op.alter_column('result',
                              existing_type=PickleType,
                              type_=MSMediumBlob)

    with op.batch_alter_table("celery_tasksetmeta") as batch_op:
        batch_op.alter_column('result',
                              existing_type=PickleType,
                              type_=MSMediumBlob)

    with op.batch_alter_table("dag_pickle") as batch_op:
        batch_op.alter_column('pickle',
                              existing_type=PickleType,
                              type_=MSMediumBlob)

    with op.batch_alter_table("dag_run") as batch_op:
        batch_op.alter_column('conf',
                              existing_type=PickleType,
                              type_=MSMediumBlob)

    with op.batch_alter_table("xcom") as batch_op:
        batch_op.alter_column('value',
                              existing_type=PickleType,
                              type_=MSMediumBlob)


def downgrade():
    pass
