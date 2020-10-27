import functools

from flask_sqlalchemy import BaseQuery, SQLAlchemy
from sqlalchemy.orm import object_session
from sqlalchemy.pool import NullPool
from sqlalchemy_searchable import make_searchable, vectorizer, SearchQueryMixin
from sqlalchemy.dialects import postgresql

from redash import settings
from redash.utils import json_dumps

db = SQLAlchemy()