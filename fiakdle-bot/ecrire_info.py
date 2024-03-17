import json
import sqlite3

DB_NAME = "fiakdle.db"
DB_URL = "../database/" + DB_NAME
ID_ETAT = 1

def ecrire_aide_sqlite(niveau_aide):
    con = sqlite3.connect(DB_URL)
    cur = con.cursor()
    requete = "UPDATE etat SET niveau_aide ="+str(niveau_aide)+" WHERE id="+str(ID_ETAT)
    cur.execute(requete)
    con.commit()
    con.close()
    print('Etat '+str(ID_ETAT)+' mis à jour => niveau_aide : '+str(niveau_aide))

def ecrire_winners_sqlite(winners_id):
    con = sqlite3.connect(DB_URL)
    cur = con.cursor()
    requete = "UPDATE etat SET winners_id ="+str(winners_id)+" WHERE id="+str(ID_ETAT)
    cur.execute(requete)
    con.commit()
    con.close()
    print('Etat '+str(ID_ETAT)+' mis à jour => winners_id : '+str(winners_id))

def ecrire_nouvelle_image_sqlite(img_url, nom_perso, nom_manga, zoom, niveau_aide, winners_id, image_buffer):
    con = sqlite3.connect(DB_URL)
    cur = con.cursor()
    requete = ("UPDATE etat SET image_url ='"+str(img_url)
    +"', nom_perso ='"+str(nom_perso)
    +"', nom_manga ='"+str(nom_manga)
    +"', zoom ='"+str(zoom)
    +"', niveau_aide ="+str(niveau_aide)
    +", winners_id ='"+str(winners_id)
    +"', image_buffer ='"+str(image_buffer)
    +"' WHERE id="+str(ID_ETAT))
    print(requete)
    cur.execute(requete)
    con.commit()
    con.close()
    
def ecrire_nouveau_jeu_sqlite(img_url, nom_perso, nom_manga, zoom, niveau_aide, channel_jeu, jeu_en_cours, winners_id, image_buffer):
    con = sqlite3.connect(DB_URL)
    cur = con.cursor()
    requete = ("UPDATE etat SET image_url ='"+str(img_url)
    +"', nom_perso ='"+str(nom_perso).replace('\'', '\'\'')
    +"', nom_manga ='"+str(nom_manga).replace('\'', '\'\'')
    +"', zoom ='"+str(zoom)
    +"', niveau_aide ="+str(niveau_aide)
    +", channel_jeu ="+str(channel_jeu)
    +", jeu_en_cours ="+str(jeu_en_cours)
    +", winners_id ='"+str(winners_id)
    +"', image_buffer ='"+str(image_buffer)
    +"' WHERE id="+str(ID_ETAT))
    print(('Etat '+str(ID_ETAT)+' mis à jour'+ 
    '\n=> image_url : '+str(img_url)+
    '\n=> nom_perso : '+str(nom_perso)+
    '\n=> nom_manga : '+str(nom_manga)+
    '\n=> zoom : '+str(zoom)+
    '\n=> niveau_aide : '+str(niveau_aide)+
    '\n=> channel_jeu : '+str(channel_jeu)+
    '\n=> jeu_en_cours : '+str(jeu_en_cours)+
    '\n=> winners_id : '+str(winners_id)+
    '\n=> image_buffer : '+str(image_buffer)
    ))

    cur.execute(requete)
    con.commit()
    con.close()

if __name__ == "__main__":
    ecrire_nouveau_jeu_sqlite(
        img_url="",
        nom_perso="",
        nom_manga="",
        zoom="",
        niveau_aide=-1,
        channel_jeu=0,
        jeu_en_cours=0,
        winners_id="",
        image_buffer=""
    )
    ecrire_nouvelle_image_sqlite(
        img_url="../images/7afba90357636da5e56b9b91a86519c27590e201.jpg",
        nom_perso="Kiyoshi Fujino;kiyoshifujino;kiyoshi;fujino",
        nom_manga="Prison School;prisonschool;purizunsukuru;kangokugakuen",
        zoom="(210,175,314,238);(171,163,349,238);(174,2,350,238);(0,0,498,237)",
        niveau_aide=-1,
        winners_id="2,4,6,8",
        image_buffer=""
    )
    ecrire_aide_sqlite(0)