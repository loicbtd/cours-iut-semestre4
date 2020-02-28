class Capteur:

    def __init__(self, duree_de_vie, zones_couvertes):
        self.__duree_de_vie = duree_de_vie
        self.__zones_couvertes = zones_couvertes

    def get_duree_de_vie(self):
        return self.__duree_de_vie

    def get_zone_couvertes(self):
        return self.__zones_couvertes
