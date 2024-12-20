import fiak
import interface_bdd

def construire_fiak(id):
    data = interface_bdd.requete_data_sqlite(id)
    if data == -1:
        return -1
    
    return fiak.Fiak(
        img_id    = data["image_id"],
        nom_perso = data["nom_perso"].split(";"),
        nom_manga = data["nom_manga"].split(";"),
        zoom      = [eval(c) for c in data["zoom"].split(";")]
    )

def recuperer_etat():
    data = interface_bdd.requete_etat_sqlite()
    if data == -1:
        return -1
    
    return fiak.Fiak(
        img_id       = data["image_id"],
        nom_perso    = data["nom_perso"].split(";"),
        nom_manga    = data["nom_manga"].split(";"),
        zoom         = [eval(c) for c in data["zoom"].split(";")],
        niveau_aide  = int(data["niveau_aide"]),
        channel_jeu  = int(data["channel_jeu"]),
        jeu_en_cours = bool(data["jeu_en_cours"]), #toute string non vide est considérée comme True, ne rien mettre pour False
        winners_id   = [] if data["winners_id"] == '' else [int(x) for x in data["winners_id"].split(";")], #à revoir en fonction de la save
        image_buffer = [] if data["image_buffer"] == '' else [int(x) for x in data["image_buffer"].split(";")] #à revoir en fonction de la save
    )

def update_fiak(fiak, id):
    data = interface_bdd.requete_data_sqlite(id)
    if data == -1:
        return -1
    
    fiak.update_fiak(
        img_id    = data["image_id"],
        nom_perso = data["nom_perso"].split(";"),
        nom_manga = data["nom_manga"].split(";"),
        zoom      = [eval(c) for c in data["zoom"].split(";")]
    )

def sauvegarder_etat(fiak):
    etat = fiak.recuperer_etat_fiak()
    interface_bdd.ecrire_nouveau_jeu_sqlite(
        img_id       = ''.join(etat['img_id']),
        nom_perso    = ';'.join(etat['nom_perso']),
        nom_manga    = ';'.join(etat['nom_manga']),
        zoom         = ';'.join(str(x) for x in etat['zoom']),
        niveau_aide  = etat['niveau_aide'],
        channel_jeu  = etat['channel_jeu'],
        jeu_en_cours = etat['jeu_en_cours'],
        winners_id   = ';'.join(str(x) for x in etat['winners_id']),
        image_buffer = ';'.join(str(x) for x in etat['image_buffer']),
    )

def sauvegarder_aide(aide):
    interface_bdd.ecrire_aide_sqlite(aide)

def sauvegarder_winners(winners):
    interface_bdd.ecrire_winners_sqlite(''.join(str(x) for x in winners))

def nb_images_bdd():
    return interface_bdd.requete_nb_images()

if __name__ == "__main__":
    print(nb_images_bdd())
    for i in range(1, 40):
        data = construire_fiak(i)
        print(data.getImgUrl())

'''
    fiak_init = construire_fiak(1)
    fiak_init.ajoutWinner(222)
    fiak_init.ajoutWinner(333)
    fiak_init.ajoutWinner(444)
    sauvegarder_etat(fiak_init)
    fiak_val = recuperer_etat()
    if fiak_init == -1 or fiak_val == 1:
        print("Ce fiak n'existe pas.")
    else:
        print(fiak_init.getImgUrl())
        print(fiak_init.getManga())
        print(fiak_init.getPerso())
        print(fiak_init.getZoom())
        print(fiak_val.getImgUrl())
        print(fiak_val.getManga())
        print(fiak_val.getPerso())
        print(fiak_val.getZoom())
        print(fiak_val.getWinners())
'''