from studio.vote import vote
from studio.utils.time_helper import timestamp_to_datetime
from studio.models import VoteInfo,VoteCandidates,VoteVotes,db
from flask import url_for,redirect,render_template,request
from faker import Faker
f=Faker(locale='zh_CN')
@vote.route('/admin/votes',methods=["GET"])
def admin_votes_show():
    voteinfo_all = VoteInfo.query.filter().all()
    return render_template(
        'vote_admin_index.html',
        info_list=voteinfo_all
        )

@vote.route('/admin/votes',methods=["POST"])#add a vote
def admin_votes_add():
    #new_vote = request.get_json()
    new_vote = request.form
    v = VoteInfo(
        title=new_vote.get("title"),
        subtitle=new_vote.get("subtitle"),
        description=new_vote.get("description"),
        image=new_vote.get("image"),
        start_at=timestamp_to_datetime(new_vote.get("start_at")),
        end_at=timestamp_to_datetime(new_vote.get("end_at")),
        vote_min=new_vote.get("vote_min"),
        vote_max=new_vote.get("vote_max"),
        admin="tzy15368@outlook.com"
    )
    #VoteInfo.add(v)
    db.session.add(v)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
    return redirect(url_for('vote.admin_votes_show'))

@vote.route('/admin/votes/<int:vote_id>',methods=["GET"])
def admin_vote_page(vote_id):
    candidate_all = VoteCandidates.query.filter(VoteCandidates.vote_id==vote_id).all()
    vote_info = VoteInfo.query.filter(VoteInfo.id==vote_id).first()
    return render_template(
        'vote_admin_vote_page.html',
        candidate_all=candidate_all,
        vote_info=vote_info,
        admin=True
    )
@vote.route('/admin/votes/<int:vote_id>/candidates',methods=["POST"])
def candidate_add(vote_id):
    new_candidate = request.form
    c = VoteCandidates(
        title=new_candidate.get("title"),
        subtitle=new_candidate.get("subtitle"),
        description=new_candidate.get("description"),
        vote_id=vote_id
    )
    db.session.add(c)
    try:
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
    return redirect(url_for('vote.admin_vote_page',vote_id=vote_id))

@vote.route('/admin/votes/<int:vote_id>/candidates/drop/<int:candidate_id>',methods=["GET"])
@vote.route('/admin/candidates/<candidate_id>',methods=["DELETE"])
def candidate_del(vote_id,candidate_id):
    VoteCandidates.query.filter(VoteCandidates.id==candidate_id).delete()
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
    return redirect(url_for('vote.admin_vote_page',vote_id=vote_id))


@vote.route('/admin/votes/drop/<vote_id>',methods=["GET"])
@vote.route('/admin/votes/<vote_id>',methods=["DELETE"])
def votes_del(vote_id):
    VoteInfo.query.filter(VoteInfo.id==vote_id).delete()
    #delete candidates and corresponding vote tickets?
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
    return redirect(url_for('vote.root'))

@vote.route('/admin/votes/<vote_id>',methods=["GET"])
def votes_details_show(vote_id):
    all = VoteVotes.query.filter(VoteVotes.id==vote_id).all()
    return render_template('vote_admin_votes.html',votes_all=all)
