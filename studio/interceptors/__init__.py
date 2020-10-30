from studio.session import session_exists
from functools import wraps
from flask import request,redirect
def session_required(func):
    @wraps(func)
    def func_wrapper(*args,**kwargs):
        sessionid = request.cookies.get('SESSIONID')
        if session_exists(sessionid):
            return func(*args,**kwargs)
        else:
            return redirect("/userservice/index?authrequired")
    return func_wrapper
