import modele.Capteur
import modele.Zone


class Situation:

    def __init__(self):
        self.__capteurs = list()
        self.__zones = list()

    def ajouter_un_capteur(self, capteur):
        self.__capteurs.append(capteur)

    def ajouter_des_capteurs(self, capteurs):
        for capteur in capteurs:
            self.ajouter_une_zone(capteur)

    def ajouter_une_zone(self, zone):
        self.__zones.append(zone)

    def ajouter_des_zones(self, zones):
        for zone in zones:
            self.ajouter_une_zone(zone)

    def lire_situation_depuis_fichier(self, chemin_relatif_fichier):
        print(chemin_relatif_fichier)
        return 1
