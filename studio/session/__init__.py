from studio import r

def session_exists(sessionid:str)->bool:
    return r.exists(sessionid)