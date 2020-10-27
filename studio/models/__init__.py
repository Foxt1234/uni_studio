import datetime
import logging
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import column_property, validates

from .mixins import TimestampMixin
from .base import db

logger = logging.getLogger(__name__)


class Alert(TimestampMixin,  db.Model):
    pass