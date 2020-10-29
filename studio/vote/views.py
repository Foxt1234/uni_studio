from studio.vote import vote
from studio.models import VoteInfo,VoteCandidates,VoteVotes,db
from flask import url_for,redirect,render_template
from faker import Faker
f=Faker(locale='zh_CN')
@vote.route("/")
def root():
    voteinfo_all = VoteInfo.query.all()
    return render_template(
        'vote_index.html',
        info_list=voteinfo_all
        )

@vote.route('/<vote_id>')
def vote_page(vote_id):
    candidate_all = VoteCandidates.query.all()
    return render_template(
        'vote_vote_page.html',
        candidate_all = candidate_all
    )
@vote.route('/populate')
def populate():
    vis = []
    for i in range(5):
        vi = VoteInfo(
            title=f.bs(),
            subtitle=f.company_suffix(),
            description=f.credit_card_full()
            )
        vis.append(vi)
    try:
        db.session.add_all(vis)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
    for v in vis:
        ci = VoteCandidates(
            title=f.bs(),
            subtitle
            )
    return redirect(url_for('vote.root'))