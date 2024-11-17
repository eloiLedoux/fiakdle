import json
import sqlite3

DB_NAME = "fiakdle.db"
DB_URL  = "../database/" + DB_NAME
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

def requete_id(db_name, id):
    con             = sqlite3.connect(DB_URL)
    con.row_factory = dict_factory
    cur             = con.cursor()
    requete         = f"SELECT * FROM {str(db_name)} WHERE id={str(id)}"
    
    cur.execute(requete)
    data = cur.fetchone()
    con.close()
    
    return data

def requete_data_sqlite(id):
    return requete_id("fiak", id)

def requete_user_sqlite(id):
    return requete_id("user", id)

def requete_etat_sqlite():
    return requete_id("etat", ID_ETAT)

def requete_nb_images():
    con     = sqlite3.connect(DB_URL)
    cur     = con.cursor()
    requete = "SELECT COUNT(*) FROM fiak;"
    
    cur.execute(requete)
    data = cur.fetchone()
    con.close()
    
    return data[0]

if __name__ == "__main__":
    print(requete_nb_images())
    for i in range(0, 10):
        data = requete_data_sqlite(i)
        print(data)