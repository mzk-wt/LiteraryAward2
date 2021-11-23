import os
from utils import db
from models import award, book, author, country

## JSONデータを作成
def generate(env):
    generateListData(env)
    generateDetailData(env)

##################################################
## 一覧用のJSONデータを作成
def generateListData(env):
    params = {
        'awards': getAwardsData(),
        'books': getBooksData(),
        'authors': getAuthorsData()
    }
    writeJsonFile(env, "award", params)
    writeJsonFile(env, "book", params)
    writeJsonFile(env, "author", params)

## 文学賞データを取得
def getAwardsData():
    list = []
    result = award.getList()
    for data in result:
        list.append({
            'id': data['id'],
            'title': data['title'],
            'kana': data['kana'],
            'countryId': data['country_id'],
            'countryName': country.getName(data['country_id']),
            'startYear': data['start_year'],
            'endYear': data['end_year'] or ""
        })
    return list

## 書籍データを取得
def getBooksData():
    list = []
    result = book.getList()
    for data in result:
        list.append({
            'id': data['id'],
            'idx': data['idx'],
            'title': data['title'],
            'kana': data['kana'],
            'author': book.getAuthorsLink(data['id']),
            'winningAward': book.getWinningAwardLink(data['id'])
        })
    return list

## 著者データを取得
def getAuthorsData():
    list = []
    result = author.getList()
    for data in result:
        list.append({
            'id': data['id'],
            'idx': data['idx'],
            'name': data['name'],
            'kana': data['kana'],
            'countryId': data['nationality_id'],
            'countryName': country.getName(data['nationality_id']),
            'winningAward': author.getWinningAwardLink(data['id'])
        })
    return list

##################################################
## 詳細画面用のJSONデータを作成
def generateDetailData(env):
    params = {
        'awardDetail': getAwardDetailData(),
        'bookDetail': getBookDetailData(),
        'authorDetail': getAuthorDetailData()
    }
    for award in params['awardDetail']:
        writeDetailJsonFile(env, "awarddetail", "awardDetail", award['id'], { 'award': award })
    for book in params['bookDetail']:
        writeDetailJsonFile(env, "bookdetail", "bookDetail", book['id'], { 'book': book })
    for author in params['authorDetail']:
        writeDetailJsonFile(env, "authordetail", "authorDetail", author['id'], { 'author': author })

## 文学賞詳細データを取得
def getAwardDetailData():
    list = []
    result = award.getList()
    for data in result:
        list.append({
            'id': data['id'],
            'title': data['title'],
            'kana': data['kana'],
            'url': data['url'],
            'countryId': data['country_id'],
            'countryName': country.getName(data['country_id']),
            'startYear': data['start_year'],
            'endYear': data['end_year'] or "",
            'overview': cnvBr(data['overview']),
            'wikipediaUrl': data['wikipedia_url'],
            'frequency': data['frequency'],
            'frequencyMonth': data['frequency_month'],
            'awardWinningWorks': getAwardWinningWorksDataBelongAward(data['id'])
        })
    return list

## 受賞作データを取得
def getAwardWinningWorksDataBelongAward(awardId):
    list = []
    aww = award.getAwardWinningWorksList(awardId)
    for w in aww:
        list.append({
            'times': w['times'],
            'awardDate': w['award_date'],
            'authorId': w['author_id'],
            'authorName': author.getName(w['author_id']),
            'bookId': w['book_id'],
            'bookTitle': book.getTitle(w['book_id'])
        })
    return list

## 書籍詳細データを取得
def getBookDetailData():
    list = []
    result = book.getList()
    for data in result:
        list.append({
            'id': data['id'],
            'title': data['title'],
            'kana': data['kana'],
            'isbn': book.getIsbn(data['id']),
            'imgUrl': data['img_url'],
            'amazonUrl': data['amazon_url'] or '',
            'kindleUrl': data['kindle_url'] or '',
            'rakutenUrl': data['rakuten_url'] or '',
            'overview': data['overview'],
            'author': book.getAuthorsLink(data['id']),
            'winningAward': book.getWinningAwardLink(data['id'])
        })
    return list

## 著者詳細データを取得
def getAuthorDetailData():
    list = []
    result = author.getList()
    for data in result:
        list.append({
            'id': data['id'],
            'name': data['name'],
            'kana': data['kana'],
            'imgUrl': data['img_url'],
            'bornDate': data['born_date'],
            'deadDate': data['dead_date'],
            'countryId': data['nationality_id'],
            'countryName': country.getName(data['nationality_id']),
            'overview': cnvBr(data['overview']),
            'wikipediaUrl': data['wikipedia_url'],
            'awardWinningWorks': getAwardWinningWorksDataBelongAuthor(data['id']) 
        })
    return list

## 著者に紐づく受賞作データを取得
def getAwardWinningWorksDataBelongAuthor(authorId):
    list = []
    aww = author.getAwardWinningWorksList(authorId)
    for w in aww:
        list.append({
            'bookId': w['book_id'],
            'bookTitle': book.getTitle(w['book_id']),
            'times': w['times'],
            'awardId': w['award_id'],
            'awardTitle': award.getTitle(w['award_id'])
        })
    return list

##################################################
## ファイル出力
def writeJsonFile(env, filename, params):
    tmpl = env.get_template("json/" + filename + ".j2")
    out = tmpl.render(params)
    f = open("output/json/" + filename + ".json", 'x')
    f.write(out)
    f.close()

## ファイル出力（詳細画面）
def writeDetailJsonFile(env, foldername, filename, fileid, params):
    tmpl = env.get_template("json/" + filename + ".j2")
    out = tmpl.render(params)
    f = open("output/json/" + foldername + "/" + filename + str(fileid) + ".json", 'x')
    f.write(out)
    f.close()

##################################################
## 改行コードを<br>に置換する
def cnvBr(value):
    return str(value).replace('\n', '<br>')

