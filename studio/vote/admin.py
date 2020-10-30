from studio.vote import vote
from studio.models import VoteInfo,VoteCandidates,VoteVotes,db
from flask import url_for,redirect,render_template
from faker import Faker
f=Faker(locale='zh_CN')

@vote.route('/admin/votes')
def votes_show():
    all = VoteVotes.query.all()
    return render_template('vote_admin_votes.html',votes_all=all)