import os
from utils import db

## 擬似RestApi実現のためのページを作成
def generate(env):
    # 書籍詳細
    result = db.select("SELECT * FROM books ORDER BY id")
    for book in result:
        params = {
            'bookId': book["id"],
            'twUrl': "http://www.literary-award-db.com/bookdetail/" + str(book["id"]),
            'twTitle': book["title"],
            'twDescription': book["overview"],
            'twImage': book["img_url"]
        }
        writeFile(env, str(book["id"]), params)

## ファイル出力
def writeFile(env, foldername, params):
    tmpl = env.get_template("rest/bookDetail.j2")
    out = tmpl.render(params)
    os.mkdir('output/rest/bookdetail/' + foldername)
    f = open("output/rest/bookdetail/" + foldername + "/index.htm", 'x')
    f.write(out)
    f.close()