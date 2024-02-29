import json
import sqlite3

DB_NAME = "fiakdle.db"
DB_URL = "../database/" + DB_NAME

def requete_data_jsonfile():
    with open('data.json', 'r') as cfg:
        data = json.load(cfg)
    if data == {}:
        return -1
    return data

def dict_factory(cursor, row):
    d= {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def requete_data_sqlite(id):
    con = sqlite3.connect(DB_URL)
    con.row_factory = dict_factory
    cur = con.cursor()
    requete = "SELECT * FROM fiak WHERE id="+str(id)
    cur.execute(requete)
    data = cur.fetchone()
    con.close()
    return data

if __name__ == "__main__":
    data_json = requete_data_jsonfile()
    data = requete_data_sqlite(1)
    print(data_json)
    print(data)