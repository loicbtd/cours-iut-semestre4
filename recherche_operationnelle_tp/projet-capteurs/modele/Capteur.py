import modele.Zone


class Capteur:

    def __init__(self, etiquette, duree_de_vie):
        self.__etiquette = etiquette
        self.__duree_de_vie = duree_de_vie
        self.__zones_couvertes = list()

    def get_etiquette(self):
        return self.__etiquette

    def get_duree_de_vie(self):
        return self.__duree_de_vie

    def ajouter_une_zone_courverte(self, zone_couverte):
        self.__zones_couvertes.append(zone_couverte)

    def ajouter_des_zones_couvertes(self, zones_couvertes):
        for zone in zones_couvertes:
            self.ajouter_une_zone_courverte(zone)
