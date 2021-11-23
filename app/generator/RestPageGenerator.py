import os
from utils import db

## 擬似RestApi実現のためのページを作成
def generate(env):
    # 書籍詳細
    result = db.select("SELECT * FROM books ORDER BY id")
    for book in result:
        writeFile(env, str(book["id"]), { 'bookId': book["id"] })

## ファイル出力
def writeFile(env, foldername, params):
    tmpl = env.get_template("rest/bookDetail.j2")
    out = tmpl.render(params)
    os.mkdir('output/rest/bookdetail/' + foldername)
    f = open("output/rest/bookdetail/" + foldername + "/index.htm", 'x')
    f.write(out)
    f.close()