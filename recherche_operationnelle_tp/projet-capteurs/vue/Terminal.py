import os
import time


class Terminal:

    def __init__(self, titre):
        self.__titre = titre
        self.__partie = ""
        self.__activite = ""

    @staticmethod
    def nettoyer():
        os.system("cls" if os.name == "nt" else "clear")

    def imprimer_en_tete(self):
        self.nettoyer()
        print(self.__titre, end='\n')
        print("[" + self.__partie + "]" if self.__partie != "" else "", end='\n')

        if self.__activite != "":
            print("\n> " + self.__activite, end='\n')

    def imprimer_message(self, message, duree):
        self.imprimer_en_tete()
        print("\n\n> "+message)
        if duree == 0:
            input()
        else:
            time.sleep(duree)
        self.nettoyer()

    def set_partie(self, partie):
        self.__partie = partie

    def set_activite(self, activite):
        self.__activite = activite

    def choisir_dans_menu(self, menu):
        (titre_menu, consigne_menu, choix_menu, choix_quitter) = menu
        self.__partie = titre_menu
        self.__activite = consigne_menu

        self.imprimer_en_tete()
        print()
        for cle, valeur in choix_menu.items():
            print(cle, " - ", valeur, end='\n')
        print("\n\t\t< q", " - ", choix_quitter, " >", end='\n')
        choix = input()
        type(choix)

        while choix not in choix_menu and choix != "q" and choix != "Q":
            self.imprimer_en_tete()
            print()
            for cle, valeur in choix_menu.items():
                print(cle, " - ", valeur, end='\n')
            print("\n\t\t< q", " - ", choix_quitter, " >", end='\n')
            choix = input()
            type(choix)

        if choix == "q" or choix == "Q":
            return None
        else:
            return int(choix)

    def choisir_fichier_dans_dossier(self, nom_dossier):
        liste_fichiers = list()
        dossier_courant = os.getcwd() + "/" + nom_dossier + "/"
        for fichier in os.listdir(dossier_courant):
            if os.path.isfile(dossier_courant + fichier):
                liste_fichiers.append(fichier)
        choix_menu = dict()
        for i in range(0, len(liste_fichiers)):
            choix_menu[str(i + 1)] = liste_fichiers[i]

        menu_choix_fichier = ("", "Choisissez un fichier à charger", choix_menu, "Retour")
        cle = self.choisir_dans_menu(menu_choix_fichier)

        if cle is None:
            return None
        else:
            cle = str(cle)
            return dossier_courant + choix_menu[cle]

    def saisir(self, donnees_ecran_saisie):
        (consigne, nature) = donnees_ecran_saisie

        self.imprimer_en_tete()
        while True:
            self.imprimer_en_tete()
            saisie = input(consigne+": ")
            (saisie, erreur) = self.valider_donnee(saisie, nature)
            if saisie is not None:
                return saisie
            else:
                print(erreur)
                time.sleep(2)
                continue

    @staticmethod
    def valider_donnee(donnee, nature):
        if nature == "entier+0":
            try:
                donnee_validee = int(donnee)
                if donnee_validee <= 0:
                    return None, "Merci de saisir un entier positif."
                return donnee_validee, ""
            except ValueError:
                return None, "Merci de saisir un entier."

        if nature == "entier+0|q":
            if donnee == "q" or donnee == "Q":
                return "q", ""
            try:
                donnee_validee = int(donnee)
                if donnee_validee <= 0:
                    return None, "Merci de saisir un entier positif ou bien 'q'."
                return donnee_validee, ""
            except ValueError:
                return None, "Merci de saisir un entier ou bien 'q'."
