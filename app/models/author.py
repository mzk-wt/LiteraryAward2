from utils import db

def getCount():
    result = db.select("SELECT count(*) AS cnt FROM authors")
    return result.fetchone()['cnt']

def getList():
    result = db.select("SELECT * FROM authors ORDER BY id")
    return result

def getName(authorId):
    if authorId is not None:
        result = db.select("SELECT name FROM authors WHERE id = %s", str(authorId))
        return result.fetchone()['name']
    else:
        return ""

def getWinningAward(authorId):
    result = db.select(
        "SELECT A.id, A.title "
        "FROM awards A, award_winning_works B " 
        "WHERE A.id = B.award_id "
        "  AND B.author_id = %s",
        str(authorId))
    list = []
    for award in result:
        list.append({
            'id': award['id'],
            'title': award['title']
        })
    return list

def getWinningAwardLink(authorId):
    waList = getWinningAward(authorId)
    link = ""
    for i, wa in enumerate(waList):
        if i > 0:
            link += "、"
        link += "<a href='../pages/award.htm?id=" + str(wa['id']) + "'>" + wa['title'] + "</a>"
    return link

def getAwardWinningWorksList(authorId):
    if authorId is not None:
        result = db.select("SELECT * FROM award_winning_works WHERE author_id = %s ORDER BY id", str(authorId))
        return result
    else:
        return []