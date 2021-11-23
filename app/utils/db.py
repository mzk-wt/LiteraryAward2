import pymysql.cursors

# MariaDB
conn = pymysql.connect(
    host='192.168.11.9',
    port=3307,
    db='LiteraryAward',
    user='admin',
    password='admin',
    cursorclass=pymysql.cursors.DictCursor)

def select(sql, params=None):
    cur = conn.cursor()
    if params is not None:
        cur.execute(sql, params)
    else:
        cur.execute(sql)
    return cur