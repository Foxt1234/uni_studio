from studio.vote import vote
@vote.route("/")
def helo():
    return "world"