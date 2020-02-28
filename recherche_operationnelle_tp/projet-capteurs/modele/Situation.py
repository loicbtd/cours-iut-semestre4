import modele.Capteur as Capteur
import vue.Terminal as Terminal
import datetime
import time
import os
import re
import pathlib

class Situation:

    def __init__(self):
        self.__capteurs = list()
        self.__zones = list()

    def lire_depuis_fichier(self, chemin_relatif_fichier):
        # ouvrir le fichier en mode lecture
        fichier = open(chemin_relatif_fichier, "r")

        # lire nombre de capteurs
        ligne = fichier.readline()
        nombre_capteurs = int(re.search(r'\d*', ligne).group())
        print("nombre_capteurs =", nombre_capteurs)

        # lire nombre de zones
        ligne = fichier.readline()
        nombre_zones = int(re.search(r'\d*', ligne).group())
        print("nombre_zones =", nombre_zones)
        self.__zones = [i for i in range(1, nombre_zones + 1)]

        # lire les durées de vie des capteurs
        ligne = fichier.readline()
        durees_de_vie = [int(i) for i in re.findall(r'\d', ligne)]
        print("durees_de_vie =", durees_de_vie)

        # lire les zones couvertes par les capteurs
        ligne = fichier.readline()
        for i in range(nombre_capteurs):
            if ligne == "":
                return -1
            zones_couvertes = [int(i) for i in re.findall(r'\d', ligne)]
            print("zones_couvertes =", zones_couvertes)
            try:
                self.__capteurs.append(Capteur.Capteur(durees_de_vie[i], zones_couvertes))
            except IndexError:
                return -1
            ligne = fichier.readline()
        # fermer le fichier
        fichier.close()
        return 0

    def saisir_manuellement(self, terminal):
        terminal.set_partie("Saisie manuelle d'une situation")
        # Saisir nombre de capteurs
        nombre_capteurs = terminal.saisir(("nombre de capteurs", "entier+0"))
        # Saisir nombre de zones
        nombre_zones = terminal.saisir(("nombre de zones", "entier+0"))
        self.__zones = [i for i in range(1, nombre_zones + 1)]
        # Pour chaque capteur
        for i in range(nombre_capteurs):
            terminal.set_activite("Capteur n° " + str(i+1))
            # Saisir duree_de_vie
            duree_de_vie = terminal.saisir(("durée de vie", "entier+0"))
            # Saisir zones couvertes
            zone_couvertes = list()
            while True:
                if set(zone_couvertes) == set(self.__zones):
                    break
                zone_a_couvrir = terminal.saisir(("Zones non couvertes: " + str([i for i in self.__zones if i not in zone_couvertes]) + "\n" + "Zones couvertes: " + str(zone_couvertes) + "\n" + "\n> Saisir une zone à couvrir (q pour finir)", "entier+0|q"))
                if zone_a_couvrir == "q":
                    break
                if zone_a_couvrir not in [i for i in self.__zones if i not in zone_couvertes]:
                    continue
                zone_couvertes.append(zone_a_couvrir)
                continue
            # ajouter capteur
            self.__capteurs.append(Capteur.Capteur(duree_de_vie, zone_couvertes))
        terminal.imprimer_message("Saisie de la situation complétée avec succès !", 2)

    def imprimer_situation(self, terminal):
        print("[Description de la situation]", end="\n\n")
        print("Nombre de capteurs: ", len(self.__capteurs), end='\n')
        print("Nombre de zones: ", len(self.__zones), end='\n')
        print("\nDurée de vie des capteurs: ", end='')
        for capteur in self.__capteurs:
            print(capteur.get_duree_de_vie(), end='')
            if capteur != self.__capteurs[-1]:
                print(end=' ')
            else:
                print()

        print("")

        # for capteur in self.__capteurs:
        #     print(*capteur.get_zones_couvertes(), sep=' ')
        #
        #     for zone in capteur.get_zones_couvertes():
        #         print("", end='')

        def sauvegarder_situation():
            chemin_dossier_sauvegarde = os.getcwd() + "/sauvegardes"
            maintenant = datetime.datetime.now()
            chemin_fichier_sauvegarde = chemin_dossier_sauvegarde + "/" + str(maintenant.year) + "-" + str(
                maintenant.month) + "-" + str(maintenant.day) + "_" + str(maintenant.hour) + "-" + str(
                maintenant.minute) + "-" + str(maintenant.second) + "_situation"
            fichier = open(chemin_fichier_sauvegarde, "a")
            fichier.write("prout")
            fichier.close()

    def sauvegarder_situation(self, nom_dossier):
        # définir le chemin depuis lequel s'execute le code
        chemin_dossier = os.getcwd() + "/" + nom_dossier
        # s'assurer que le dossier de sauvegarde existe si non le créer
        pathlib.Path(chemin_dossier).mkdir(parents=True, exist_ok=True)
        # définir le nom du fichier
        maintenant = datetime.datetime.now()
        nom_fichier = str(maintenant.year) + "-" + str(maintenant.month) + "-" + str(maintenant.day) + "_" + str(maintenant.hour) + "-" + str(maintenant.minute) + "-" + str(maintenant.second) + "_situation"
        # créer et ouvrir le fichier
        try:
            fichier = open(chemin_dossier + "/" + nom_fichier, "x")
        except FileExistsError:
            return
        # écrire la situation dans le fichier
        fichier.write(str(len(self.__capteurs)))
        fichier.write("\n"+str(len(self.__zones)))
        fichier.write("\n")
        for capteur in self.__capteurs:
            if capteur != self.__capteurs[-1]:
                fichier.write(str(capteur.get_duree_de_vie()) + " ")
            else:
                fichier.write(str(capteur.get_duree_de_vie()))
        for capteur in self.__capteurs:
            fichier.write("\n")
            for zone in capteur.get_zone_couvertes():
                if zone != capteur.get_zone_couvertes()[-1]:
                    fichier.write(str(zone) + " ")
                else:
                    fichier.write(str(zone))
        fichier.close()



