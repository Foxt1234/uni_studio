from flask import Blueprint
vote = Blueprint("vote",__name__,url_prefix='/vote')

from studio.vote import views
@vote.route('/bbb')
def bbb():
    return 'bbb'