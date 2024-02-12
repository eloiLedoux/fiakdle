import fiak
import recup_info

def construire_fiak():
    data = recup_info.requete_data()
    if data == -1:
        #ID associé à aucune carte
        return -1
    return fiak.Fiak(
        img_url=data["img_url"],
        nom_perso=data["nom_perso"].split(";"),
        nom_manga=data["nom_manga"].split(";"),
        #zoom=data["zoom"].split(";")
        zoom=[eval(c) for c in data["zoom"].split(";")]
    )

if __name__ == "__main__":
    fiak = construire_fiak()
    if fiak == -1:
        print("Ce fiak n'existe pas.")
    else:
        print(fiak.getImgUrl())
        print(fiak.getManga())
        print(fiak.getPerso())
        print(fiak.getZoom())