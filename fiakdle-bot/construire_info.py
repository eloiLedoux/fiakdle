import fiak
import recup_info

def construire_fiak(id):
    data = recup_info.requete_data_sqlite(id)
    if data == -1:
        return -1
    return fiak.Fiak(
        img_url=data["image_url"],
        nom_perso=data["nom_perso"].split(";"),
        nom_manga=data["nom_manga"].split(";"),
        zoom=[eval(c) for c in data["zoom"].split(";")]
    )

def recuperer_fiak():
    data = recup_info.requete_data_jsonfile()
    if data == -1:
        return -1
    return fiak.Fiak(
        img_url=data["image_url"],
        nom_perso=data["nom_perso"].split(";"),
        nom_manga=data["nom_manga"].split(";"),
        zoom=[eval(c) for c in data["zoom"].split(";")],
        niveau_aide=int(data["niveau_aide"]),
        channel_jeu=int(data["channel_jeu"]),
        jeu_en_cours=bool(data["jeu_en_cours"]), #toute string non vide est considérée comme True, ne rien mettre pour False
        winners_id=data["winners_id"].split(";"), #à revoir en fonction de la save
        image_buffer=data["image_buffer"].split(";"), #à revoir en fonction de la save
    )

def update_fiak(fiak, id):
    data = recup_info.requete_data_sqlite(id)
    if data == -1:
        return -1
    fiak.update_fiak(
        img_url=data["image_url"],
        nom_perso=data["nom_perso"].split(";"),
        nom_manga=data["nom_manga"].split(";"),
        zoom=[eval(c) for c in data["zoom"].split(";")]
    )

if __name__ == "__main__":
    fiak = construire_fiak(1)
    if fiak == -1:
        print("Ce fiak n'existe pas.")
    else:
        print(fiak.getImgUrl())
        print(fiak.getManga())
        print(fiak.getPerso())
        print(fiak.getZoom())