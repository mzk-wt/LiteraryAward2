import pymysql.cursors

# MariaDB
conn = pymysql.connect(
    host='mysql62.conoha.ne.jp',
    db='p5klt_ladb',
    user='p5klt_ladb',
    password='YQLVy@L@hRvU8tw',
    cursorclass=pymysql.cursors.DictCursor)

def select(sql, params=None):
    cur = conn.cursor()
    if params is not None:
        cur.execute(sql, params)
    else:
        cur.execute(sql)
    return cur

#result = select("SELECT * FROM TEST WHERE ID = %s", [1])
#result = select("SELECT * FROM authors where id=1")
#for rowData in result:
#    print(rowData)
