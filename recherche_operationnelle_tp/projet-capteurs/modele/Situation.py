import modele.Capteur as Capteur
import vue.Terminal as Terminal
import datetime
import time
import os
import re
import pathlib
import glpk


class Situation:

    def __init__(self):
        self.__capteurs = list()
        self.__zones = list()

    def lire_depuis_fichier(self, chemin_absolu_fichier):
        # ouvrir le fichier en mode lecture
        fichier = open(chemin_absolu_fichier, "r")
        # lire nombre de capteurs
        ligne = fichier.readline()
        nombre_capteurs = int(re.search(r'\d*', ligne).group())
        # lire nombre de zones
        ligne = fichier.readline()
        nombre_zones = int(re.search(r'\d*', ligne).group())
        self.__zones = [i for i in range(1, nombre_zones + 1)]
        # lire les durées de vie des capteurs
        ligne = fichier.readline()
        durees_de_vie = [int(i) for i in re.findall(r'\d', ligne)]
        # lire les zones couvertes par les capteurs
        ligne = fichier.readline()
        for i in range(nombre_capteurs):
            if ligne == "":
                return -1
            zones_couvertes = [int(i) for i in re.findall(r'\d', ligne)]
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
            terminal.set_activite("Capteur n° " + str(i + 1))
            # Saisir duree_de_vie
            duree_de_vie = terminal.saisir(("durée de vie", "entier+0"))
            # Saisir zones couvertes
            zone_couvertes = list()
            while True:
                if set(zone_couvertes) == set(self.__zones):
                    break
                zone_a_couvrir = terminal.saisir(("Zones non couvertes: " + str(
                    [i for i in self.__zones if i not in zone_couvertes]) + "\n" + "Zones couvertes: " + str(
                    zone_couvertes) + "\n" + "\n> Saisir une zone à couvrir (q pour finir)", "entier+0|q"))
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
        en_tete = ['Capteurs', 'Zones couvertes', 'Durée de vie (en unité de temps)']
        lignes = []
        for capteur in self.__capteurs:
            ligne = ["S" + str(self.__capteurs.index(capteur) + 1),
                     ', '.join(["Z" + str((zone)) for zone in capteur.get_zone_couvertes()]),
                     "T" + str(self.__capteurs.index(capteur) + 1) + " = " + str(capteur.get_duree_de_vie())]
            lignes.append(ligne)
        terminal.imprimer_tableau(en_tete, lignes)

    def sauvegarder_situation(self, nom_dossier):
        # définir le chemin depuis lequel s'execute le code
        chemin_dossier = os.getcwd() + "/" + nom_dossier
        # s'assurer que le dossier de sauvegarde existe si non le créer
        pathlib.Path(chemin_dossier).mkdir(parents=True, exist_ok=True)
        # définir le nom du fichier
        maintenant = datetime.datetime.now()
        nom_fichier = str(maintenant.year) + "-" + str(maintenant.month) + "-" + str(maintenant.day) + "_" + str(
            maintenant.hour) + "-" + str(maintenant.minute) + "-" + str(maintenant.second) + "_situation"
        # créer et ouvrir le fichier
        try:
            fichier = open(chemin_dossier + "/" + nom_fichier, "x")
        except FileExistsError:
            return
        # écrire la situation dans le fichier
        fichier.write(str(len(self.__capteurs)))
        fichier.write("\n" + str(len(self.__zones)))
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

    @staticmethod
    def generer_toutes_les_configurations(elements):
        toutes_les_configurations = []
        for i in range(2 ** len(elements)):
            configuration = []
            for j in range(len(elements)):
                if (i & (1 << j)) != 0:
                    configuration.append(elements[j])
            if configuration not in toutes_les_configurations:
                toutes_les_configurations.append(configuration)
        return toutes_les_configurations

    def __est_configuration_valide(self, configuration):
        zones_couvertes = []
        for indice_capteur in configuration:
            for zone_couverte in self.__capteurs[indice_capteur].get_zone_couvertes():
                if zone_couverte not in zones_couvertes:
                    zones_couvertes.append(zone_couverte)
                if set(zones_couvertes) == set(self.__zones):
                    return True
        return False

    def __generer_configurations_valides(self, configurations):
        configurations_valides = []
        for configuration in configurations:
            if self.__est_configuration_valide(configuration):
                configurations_valides.append(configuration)
        return configurations_valides

    def __generer_configurations_elementaires(self, configurations):
        configurations_elementaires = []
        # pour chaque configuration
        for configuration in configurations:
            compteur_configurations_valides = 0
            for sous_configuration in self.generer_toutes_les_configurations(configuration):
                if self.__est_configuration_valide(sous_configuration):
                    compteur_configurations_valides += 1
            if compteur_configurations_valides == 1:
                configurations_elementaires.append(configuration)
        return configurations_elementaires

    def traiter_la_situation(self, terminal):
        # trouver tous les sous ensembles / configurations
        toutes_les_configurations = self.generer_toutes_les_configurations(range(0, len(self.__capteurs)))
        # trouver toutes les configurations valides
        configurations_valides = self.__generer_configurations_valides(toutes_les_configurations)
        # trouver toutes les configurations valides élémentaires
        configurations_valides_elementaires = self.__generer_configurations_elementaires(configurations_valides)

        terminal.set_partie("Impression de la situation et de ses configurations élémentaires")
        terminal.set_activite("")
        terminal.imprimer_en_tete()
        terminal.imprimer("\n\n")
        self.imprimer_situation(terminal)
        terminal.imprimer("\n\n> Configurations élémentaires:\n\n")

        en_tete = ['Configurations élémentaires']
        lignes = []
        for configuration_valide_elementaire in configurations_valides_elementaires:
            ligne = [
                ', '.join(["S" + str((indice_capteur + 1)) for indice_capteur in configuration_valide_elementaire])]
            lignes.append(ligne)
        terminal.imprimer_tableau(en_tete, lignes)
        terminal.imprimer("\n\n\t\t< Appuyer sur entrer pour passer >\n")
        input()

    def resoudre_situation(self, terminal):
        # trouver tous les sous ensembles / configurations
        toutes_les_configurations = self.generer_toutes_les_configurations(range(0, len(self.__capteurs)))
        # trouver toutes les configurations valides
        configurations_valides = self.__generer_configurations_valides(toutes_les_configurations)
        # trouver toutes les configurations valides élémentaires
        configurations_valides_elementaires = self.__generer_configurations_elementaires(configurations_valides)

        probleme = glpk.LPX()
        probleme.name = 'Maximiser la durée de vie du réseau'
        probleme.obj.maximize = True

        probleme.rows.add(len(self.__capteurs))  # Ajouter autant de contraintes que de capteurs
        for ligne in probleme.rows:  # Pour chaque contrainte liée à un capteur
            ligne.name = "Contrainte des configurations contenant le capteur S" + str(ligne.index + 1)  # Nommer la contrainte
            probleme.rows[ligne.index].bounds = None, float(
                self.__capteurs[ligne.index].get_duree_de_vie())  # Set bound -inf < C1 <= durée de vie du capteur

        probleme.cols.add(
            len(configurations_valides_elementaires))  # Ajouter autant de colonnes (variables que de configurations
        for colonne in probleme.cols:  # Pour toutes les colonnes
            colonne.name = 'tu%d' % colonne.index  # Les nommer tu1, tu2, ..., tuN
            colonne.bounds = 0.0, None  # La durée ne peut pas être négative

        probleme.obj[:] = [1.0]*len(configurations_valides_elementaires)  # Initialiser tous les coefficients de la fonction objectif à 1.0

        # définir matrice des coefficients pour capteur pour chaque configuration
        matrice_coefficients = []
        for indice_capteur in range(len(self.__capteurs)):  # pour chaque capteur
            for configuration in configurations_valides_elementaires:  # pour chaque configuration
                if indice_capteur in configuration:
                    matrice_coefficients.append(1.0)  # si le capteur est présent, alors son coefficien vaut 1
                else:
                    matrice_coefficients.append(0.0)  # si le capteur est absent, alors son coefficien vaut 0
        probleme.matrix = matrice_coefficients  # affecter la matrice des coeffecients au problème

        probleme.simplex()  # résoudre le problème avec la méthode du simplex
        #
        # duree_de_vie_optimale = probleme.obj.value  # récupérer la durée de vie optimale
        #
        # print('; '.join('%s = %g' % (c.name, c.primal) for c in probleme.cols))  # Print struct variable names and primal values

        terminal.set_partie("Maximiser la durée de vie du réseau")
        terminal.imprimer_en_tete()
        terminal.imprimer("\nSituation:\n")
        self.imprimer_situation(terminal)

        terminal.imprimer("\nSoit t1, t2, t3")


        terminal.imprimer("\n\n\t\t< Appuyer sur entrer pour passer >\n")
        input()