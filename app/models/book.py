from utils import db

def getCount():
    result = db.select("SELECT count(*) AS cnt FROM books")
    return result.fetchone()['cnt']

def getList():
    result = db.select("SELECT * FROM books ORDER BY id")
    return result

def getTitle(bookId):
    if bookId is not None:
        result = db.select("SELECT title FROM books WHERE id = %s", str(bookId))
        return result.fetchone()['title']
    else:
        return ""

def getIsbn(bookId):
    if bookId is not None:
        result = db.select("SELECT isbn FROM books WHERE id = %s", str(bookId))
        isbn = result.fetchone()['isbn']
        if isbn is None or isbn.startswith('ASIN'):
            return ""
        else:
            return isbn
    else:
        return ""

def getAuthors(bookId):
    if bookId is not None:
        result = db.select(
            "SELECT B.id, B.name, A.role FROM book_authors A, authors B "
            "WHERE A.author_id = B.id "
            "  AND A.book_id = %s",
            str(bookId))
        return result
    else:
        return ""

def getAuthorsLink(bookId, rootpath = '../'):
    authorList = getAuthors(bookId)
    link = ""
    for i, author in enumerate(authorList):
        if i > 0:
            link += '、'
        link += "<a href='" + rootpath + "pages/author.htm?id=" + str(author['id']) + "'>" + author['name'] + "(" + author['role'] + ")" + "</a>"
    return link

def getWinningAward(bookId):
    result = db.select(
        "SELECT A.id, A.title "
        "FROM awards A, award_winning_works B " 
        "WHERE A.id = B.award_id "
        "  AND B.book_id = %s",
        str(bookId))
    list = []
    for award in result:
        list.append({
            'id': award['id'],
            'title': award['title']
        })
    return list

def getWinningAwardLink(bookId, rootpath = '../'):
    waList = getWinningAward(bookId)
    link = ""
    for i, wa in enumerate(waList):
        if i > 0:
            link += "、"
        link += "<a href='" + rootpath + "pages/award.htm?id=" + str(wa['id']) + "'>" + wa['title'] + "</a>"
    return link

def getWhatsNew(limit):
    news = []
    result = db.select("SELECT id, title, img_url, DATE_FORMAT(created_at, '%Y/%m/%d') AS created_at FROM books ORDER BY created_at DESC LIMIT " + str(limit))
    for book in result:
        authors = getAuthorsLink(book["id"], './')
        awards = getWinningAwardLink(book["id"], './')
        news.append({
            'bookId': book["id"],
            'bookTitle': book["title"],
            'bookImgUrl': book["img_url"],
            'authors': authors,
            'awards': awards,
            'createdAt': book["created_at"]
        })

    return news