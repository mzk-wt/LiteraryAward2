from utils import db

def getList():
    result = db.select("SELECT * FROM awards ORDER BY id")
    return result

def getTitle(awardId):
    if awardId is not None:
        result = db.select("SELECT title FROM awards WHERE id = %s", str(awardId))
        return result.fetchone()['title']
    else:
        return ""

def getAwardWinningWorksList(awardId):
    if awardId is not None:
        result = db.select("SELECT * FROM award_winning_works WHERE award_id = %s ORDER BY id", str(awardId))
        return result
    else:
        return []
