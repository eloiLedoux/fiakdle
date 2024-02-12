import cropper

def gen_fiak_zoom(chemin_image, zoom):
    chemin_fiak = "../images/fiak-du-jour.jpg"
    cropper.crop_image(chemin_image, chemin_fiak, zoom)

if __name__ == "__main__":
    chemin_image = "../images/1.jpg"
    zoom = eval("(481,420,674,572)")  #L'argument zoom ne devrait pas être des coordonnées mais un indice permettant de récupérer les coordonnées corespondantes dans le json.
    gen_fiak_zoom(chemin_image=chemin_image, zoom=zoom)