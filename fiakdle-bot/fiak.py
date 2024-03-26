NB_IMAGES_BDD = 11

class Fiak:
    def __init__(self, img_url, nom_perso, nom_manga, zoom, niveau_aide = -1, channel_jeu = None, jeu_en_cours = False, winners_id = [], image_buffer = []):
        self.img_url = img_url

        #Liste de noms acceptés (permet de gérer le cas où plusieurs écritures
        #sont possibles pour un même perso, ex : Luffy, luffy, monkeydluffy, monkeyluffy).
        #Le nom d'affichage du perso sera toujours le premier nom de la liste.
        self.nom_perso = nom_perso
        #Liste de noms acceptés (permet de gérer le cas où plusieurs écritures
        #sont possibles pour un même manga, ex : Demon Slayer, demonslayer, kimetsunoyaiba).
        #Le nom d'affichage du manga sera toujours le premier nom de la liste.
        self.nom_manga = nom_manga
        self.zoom = zoom
        self.niveau_aide = niveau_aide 
        self.channel_jeu = channel_jeu
        self.jeu_en_cours = jeu_en_cours #actuellement obsolète
        self.winners_id = winners_id
        self.image_buffer = image_buffer

    def recuperer_etat_fiak(self):
        etat = {
            'img_url' : self.img_url,
            'nom_perso' : self.nom_perso,
            'nom_manga' : self.nom_manga,
            'zoom' : self.zoom,
            'niveau_aide' : self.niveau_aide,
            'channel_jeu' : self.channel_jeu if self.channel_jeu else 0,
            'jeu_en_cours' : 1 if self.jeu_en_cours else 0,
            'winners_id' : self.winners_id,
            'image_buffer' : self.image_buffer
        }
        return etat

    def guessFiak(self, reponseChar, reponseManga):
        if(reponseChar in self.nom_perso and reponseManga in self.nom_manga):
            return True, True
        elif (reponseChar not in self.nom_perso and reponseManga in self.nom_manga):
            return False, True
        elif (reponseChar in self.nom_perso and reponseManga not in self.nom_manga):
            return True, False
        return False, False

    def update_fiak(self, img_url, nom_perso, nom_manga, zoom):
        self.img_url = img_url
        self.nom_perso = nom_perso
        self.nom_manga = nom_manga
        self.zoom = zoom
    
    def augmenterAide(self):
        self.niveau_aide = (self.niveau_aide + 1) % 4

    def ajoutWinner(self, winner):
        self.winners_id.append(winner)

    def clearWinner(self):
        self.winners_id.clear()

    def getWinners(self):
        return self.winners_id

    def hasWinner(self):
        return True if self.winners_id else False

    def ajoutBuffer(self, image):
        if len(self.image_buffer) > 30:
            self.image_buffer.pop(0)
        self.image_buffer.append(image)

    def estDansBuffer(self, image):
        if image in self.image_buffer:
            return True
        return False

    def clearBuffer(self):
        self.image_buffer.clear()

    def getImgUrl(self):
        return self.img_url

    def getAide(self):
        return self.niveau_aide

    def setAide(self, aide):
        self.niveau_aide = aide % 4

    def getManga(self):
        return self.nom_manga[0]
    
    def getPerso(self):
        return self.nom_perso[0]

    def getZoom(self):
        return self.zoom[self.niveau_aide]

    def hasChannelJeu(self):
        if self.channel_jeu and self.channel_jeu != 0: 
            return True
        return False

    def setChannelJeu(self, ch):
        self.channel_jeu = ch

    def getChannelJeu(self):
        return self.channel_jeu

    def getJeuEnCours(self):
        return self.jeu_en_cours

    def setJeuEnCours(self, bool):
        self.jeu_en_cours = bool