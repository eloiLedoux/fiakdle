import json
import sqlite3

DB_NAME = "fiakdle.db"
DB_URL  = "../database/" + DB_NAME
ID_ETAT = 1

#LECTURE
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

def select_sqlite(requete):
    con             = sqlite3.connect(DB_URL)
    con.row_factory = dict_factory
    cur             = con.cursor()
    
    cur.execute(requete)
    data = cur.fetchone()
    con.close()
    
    return data

def select_id(db_name, id):
    requete = f"SELECT * FROM {str(db_name)} WHERE id={str(id)}"

    return select_sqlite(requete=requete)

def requete_data_sqlite(id):
    return select_id("fiak", id)

def requete_etat_sqlite():
    return select_id("etat", ID_ETAT)

def requete_nb_images():
    requete = "SELECT COUNT(*) FROM fiak;"
    
    return select_sqlite(requete=requete)["COUNT(*)"]

def requete_serveur_sqlite(id):
    requete = f"SELECT * FROM server WHERE server_id={str(id)}"
    
    return select_sqlite(requete=requete)

def requete_presence_serveur(id_serveur):
    requete = "SELECT COUNT(*) FROM server WHERE server_id = "+str(id_serveur)
    
    return True if select_sqlite(requete=requete)["COUNT(*)"] == 1 else False


#ECRITURE
def update_sqlite(requete):
    con     = sqlite3.connect(DB_URL)
    cur     = con.cursor()

    cur.execute(requete)
    con.commit()
    con.close()

def ecrire_aide_sqlite(niveau_aide):
    requete = (
        "UPDATE etat SET niveau_aide ="+str(niveau_aide)
        +" WHERE id="                  +str(ID_ETAT)
    )
    
    update_sqlite(requete=requete)
    
    print('Etat '+str(ID_ETAT)+' mis à jour => niveau_aide : '+str(niveau_aide))

def ecrire_winners_sqlite(winners_id):
    requete = (
        "UPDATE etat SET winners_id ="+str(winners_id)
        +" WHERE id="                 +str(ID_ETAT)
    )
    
    update_sqlite(requete=requete)
    
    print('Etat '+str(ID_ETAT)+' mis à jour => winners_id : '+str(winners_id))

def ecrire_nouvelle_image_sqlite(img_id, nom_perso, nom_manga, zoom, niveau_aide, winners_id, image_buffer):
    requete = (
        "UPDATE etat SET image_id ='"+str(img_id)
        +"', nom_perso ='"           +str(nom_perso)
        +"', nom_manga ='"           +str(nom_manga)
        +"', zoom ='"                +str(zoom)
        +"', niveau_aide ="          +str(niveau_aide)
        +", winners_id ='"           +str(winners_id)
        +"', image_buffer ='"        +str(image_buffer)
        +"' WHERE id="               +str(ID_ETAT)
    )
    print(requete)
    
    update_sqlite(requete=requete)
    
def ecrire_nouveau_jeu_sqlite(img_id, nom_perso, nom_manga, zoom, niveau_aide, channel_jeu, jeu_en_cours, winners_id, image_buffer):
    requete = (
        "UPDATE etat SET image_id ='"+str(img_id)
        +"', nom_perso ='"           +str(nom_perso).replace('\'', '\'\'')
        +"', nom_manga ='"           +str(nom_manga).replace('\'', '\'\'')
        +"', zoom ='"                +str(zoom)
        +"', niveau_aide ="          +str(niveau_aide)
        +", channel_jeu ="           +str(channel_jeu)
        +", jeu_en_cours ="          +str(jeu_en_cours)
        +", winners_id ='"           +str(winners_id)
        +"', image_buffer ='"        +str(image_buffer)
        +"' WHERE id="               +str(ID_ETAT)
    )
    print((
        'Etat '+str(ID_ETAT)   +' mis à jour'+ 
        '\n=> image_id : '     +str(img_id)+
        '\n=> nom_perso : '    +str(nom_perso)+
        '\n=> nom_manga : '    +str(nom_manga)+
        '\n=> zoom : '         +str(zoom)+
        '\n=> niveau_aide : '  +str(niveau_aide)+
        '\n=> channel_jeu : '  +str(channel_jeu)+
        '\n=> jeu_en_cours : ' +str(jeu_en_cours)+
        '\n=> winners_id : '   +str(winners_id)+
        '\n=> image_buffer : ' +str(image_buffer)
    ))

    update_sqlite(requete=requete)

def ajouter_serveur_sqlite():
    pass

def activer_serveur_sqlite(server_id, game_chan_id, reg_chan_id, reg_msg_id):
    #INSERT OR REPLACE INTO server (server_id, game_chan_id, reg_chan_id, reg_msg_id, active) VALUES (101, 1,1,1,1)

    requete = (
        "INSERT OR REPLACE INTO server (server_id, game_chan_id, reg_chan_id, reg_msg_id, active)"
        +"VALUES (" +str(server_id)
        +", "       +str(game_chan_id)
        +", "       +str(reg_chan_id)
        +", "       +str(reg_msg_id)
        +", 1);"               
    )

    update_sqlite(requete=requete)

def desactiver_serveur_sqlite(server_id):
    requete = (
        "INSERT OR REPLACE INTO server (server_id, game_chan_id, reg_chan_id, reg_msg_id, active)"
        +"VALUES (" +str(server_id)
        +", "       +str(0)
        +", "       +str(0)
        +", "       +str(0)
        +", 0);"               
    )

    update_sqlite(requete=requete)

if __name__ == "__main__":
    print(requete_data_sqlite(1))
    print(requete_etat_sqlite())
    print(requete_nb_images())
    print(requete_presence_serveur(1))
    print(requete_serveur_sqlite(1))

    # ecrire_nouveau_jeu_sqlite(
    #     img_id       = "",
    #     nom_perso    = "",
    #     nom_manga    = "",
    #     zoom         = "",
    #     niveau_aide  = -1,
    #     channel_jeu  = 0,
    #     jeu_en_cours = 0,
    #     winners_id   = "",
    #     image_buffer = ""
    # )

    # ecrire_nouvelle_image_sqlite(
    #     img_id       = "7afba90357636da5e56b9b91a86519c27590e201",
    #     nom_perso    = "Kiyoshi Fujino;kiyoshifujino;kiyoshi;fujino",
    #     nom_manga    = "Prison School;prisonschool;purizunsukuru;kangokugakuen",
    #     zoom         = "(210,175,314,238);(171,163,349,238);(174,2,350,238);(0,0,498,237)",
    #     niveau_aide  = -1,
    #     winners_id   = "",
    #     image_buffer = ""
    # )

    activer_serveur_sqlite(34,3,4,5)
    activer_serveur_sqlite(2,3,3,3)
    desactiver_serveur_sqlite(2)
    activer_serveur_sqlite(100,1,1,1)