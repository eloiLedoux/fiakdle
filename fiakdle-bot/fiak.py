class Fiak:
    def __init__(self, img_url, nom_perso, nom_manga, zoom):
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
        self.niveau_aide = -1 #Afin qu'au lancement, le premier appel à augmenterAide place le mécanisme en fonctionnement
        self.channelJeu = None

    def guessFiak(self, reponseChar, reponseManga):
        if(reponseChar in self.nom_perso and reponseManga in self.nom_manga):
            return True, True
        elif (reponseChar not in self.nom_perso and reponseManga in self.nom_manga):
            return False, True
        elif (reponseChar in self.nom_perso and reponseManga not in self.nom_manga):
            return True, False
        return False, False
    
    def augmenterAide(self):
        print(self.niveau_aide)
        self.niveau_aide = (self.niveau_aide + 1) % 4

    def getImgUrl(self):
        return self.img_url

    def getAide(self):
        return self.niveau_aide

    def getManga(self):
        return self.nom_manga[0]
    
    def getPerso(self):
        return self.nom_perso[0]

    def getZoom(self):
        return self.zoom[self.niveau_aide]

    def hasChannelJeu(self):
        if self.channelJeu: return True; return False

    def setChannelJeu(self, ch):
        self.channelJeu = ch

    def getChannelJeu(self):
        return self.channelJeu