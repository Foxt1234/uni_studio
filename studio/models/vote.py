from .base import db
from .mixins import TimestampMixin
class VoteVotes(TimestampMixin,db.Model):
    __tablename__="vote_voters"
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(100))
    candidate = db.Column(db.Integer())#candidates id
    vote_id = db.Column(db.Integer())#vote info id



class VoteCandidates(TimestampMixin,db.Model):
    __tablename__ = "vote_candidates"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255),nullable=True)
    subtitle = db.Column(db.String(255),nullable=True)
    description = db.Column(db.String(255),nullable=True)
    action_at = db.Column(db.DateTime(True), default=db.func.now(), nullable=True)
    votes = db.Column(db.Integer,nullable=False)
    vote_id = db.Column(db.Integer,nullable=False)

    def __init__(self,*args,**kwargs):
        super(VoteCandidates, self).__init__(**kwargs)
    def __str__(self):
        return "<Candidate NO {}>".format(self.id)

class VoteInfo(TimestampMixin,db.Model):
    __tablename__ = "vote_info"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255),nullable=False)
    subtitle = db.Column(db.String(255),nullable=True)
    description = db.Column(db.String(255),nullable=True)
    disabled = db.Column(db.Boolean, default=False, nullable=False)
    start_at = db.Column(db.DateTime(True), default=db.func.now(), nullable=True)
    end_at = db.Column(db.DateTime(True), default=db.func.now(), nullable=True)
    
    def __init__(self,*args,**kwargs):
        super(VoteInfo, self).__init__(**kwargs)
    def __str__(self):
        return "<Vote NO {}>".format(self.id)
    def add(self,info):
        try:
            db.session.add(info)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()


    def badd_all(self,info_list:list):
        try:
            db.session.add_all(info_list)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()