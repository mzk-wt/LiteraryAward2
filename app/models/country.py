from utils import db

def getName(countryId):
    if countryId is not None:
        result = db.select("SELECT name_jp FROM countries WHERE id = %s", str(countryId))
        return result.fetchone()['name_jp']
    else:
        return ""
