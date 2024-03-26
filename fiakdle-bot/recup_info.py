import json
import sqlite3

DB_NAME = "fiakdle.db"
DB_URL = "../database/" + DB_NAME
ID_ETAT = 1

def requete_data_jsonfile():
    with open('save.json', 'r') as cfg:
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

def requete_etat_sqlite():
    con = sqlite3.connect(DB_URL)
    con.row_factory = dict_factory
    cur = con.cursor()
    requete = "SELECT * FROM etat WHERE id="+str(ID_ETAT)
    cur.execute(requete)
    data = cur.fetchone()
    con.close()
    return data

def requete_nb_images():
    con = sqlite3.connect(DB_URL)
    cur = con.cursor()
    requete = "SELECT COUNT(*) FROM fiak;"
    cur.execute(requete)
    data = cur.fetchone()
    con.close()
    return data[0]

if __name__ == "__main__":
    print(requete_nb_images())
    for i in range(0, 40):
        data = requete_data_sqlite(i)
        print(data)

'''
    data_json = requete_data_jsonfile()
    data = requete_data_sqlite(1)
    etat = requete_etat_sqlite()
    print(data_json)
    print(data)
    print(etat)
'''