from sqlalchemy.event import listens_for

from .base import db, Column

class TimestampMixin(object):
    updated_at = Column(db.DateTime(True), default=db.func.now(), nullable=False)
    created_at = Column(db.DateTime(True), default=db.func.now(), nullable=False)

