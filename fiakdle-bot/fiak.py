class Fiak:
    def __init__(self, img_url, nom_perso, nom_manga):
        self.img_url = img_url

        #Liste de noms acceptés (permet de gérer le cas où plusieurs écritures
        #sont possibles pour un même perso, ex : Luffy, luffy, monkeydluffy, monkeyluffy).
        #Le nom d'affichage du perso sera toujours le premier nom de la liste.
        self.nom_perso = nom_perso
        #Liste de noms acceptés (permet de gérer le cas où plusieurs écritures
        #sont possibles pour un même manga, ex : Demon Slayer, demonslayer, kimetsunoyaiba).
        #Le nom d'affichage du manga sera toujours le premier nom de la liste.
        self.nom_manga = nom_manga

    def guessFiak(self, reponseChar, reponseManga):
        if(reponseChar in self.nom_perso and reponseManga in self.nom_manga):
            return True, True
        elif (reponseChar not in self.nom_perso and reponseManga in self.nom_manga):
            return False, True
        elif (reponseChar in self.nom_perso and reponseManga not in self.nom_manga):
            return True, False
        return False, False

    def getImgUrl(self):
        return self.img_url

    def getManga(self):
        return self.nom_manga[0]
    
    def getPerso(self):
        return self.nom_perso[0]