from .base import db,Column,primary_key
from .mixins import TimestampMixin
class VoteVoters(TimestampMixin,db.Model):
    __tablename__="vote_voters"
    id = primary_key()


class VoteCandidates(TimestampMixin,db.Model):
    __tablename__ = "vote_candidates"
    id = primary_key()
    title = Column(db.String(255))
    subtitle = Column(db.String(255))
    description = Column(db.String(255))
    action_at = Column(db.DateTime(True), default=db.func.now(), nullable=True)
    votes = Column(db.Integer(20))

class VoteInfo(TimestampMixin,db.Model):
    __tablename__ = "vote_info"
    id = primary_key()