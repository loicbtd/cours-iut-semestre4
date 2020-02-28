from modele.Situation import *

menu_principal = ("Menu Principal",
                  "Choisissez une action:",
                  {'1': 'Créer manuellement une situation',
                   '2': 'Charger une situation à partir d\'un fichier'},
                  "Quitter")

menu_situation = ("Menu Situation",
                  "Choisissez une action: ",
                  {'1': 'Afficher configurations élémentaires',
                   '2': 'Écrire le programme linéaire correspondant au problème d\'ordonnancement et le résoudre avec le solveur GLPK',
                   '3': 'Analyse des résultats',
                   '4': 'Sauvegarder la situation'},
                  "Retour")


def start_program():
    terminal = Terminal.Terminal("Projet : Problème d'activation de capteurs pour surveillance de zones")

    terminal.imprimer_message("\t\t\t\tBienvenue !\n\n\n\n\t\t\t® Loïc BERTRAND - 2020  ", 0)

    while True:
        situation = Situation()
        action = terminal.choisir_dans_menu(menu_principal)
        if action == 1:
            situation.saisir_manuellement(terminal)
        if action == 2:
            chemin_fichier = terminal.choisir_fichier_dans_dossier("donnee")
            if chemin_fichier is None:
                continue
            if situation.lire_depuis_fichier(chemin_fichier) != 0:
                continue
        if action is None:
            break

        boucle_secondaire = True
        while boucle_secondaire:
            action = terminal.choisir_dans_menu(menu_situation)
            if action == 1:
                situation.afficher_configurations_elemetaires(terminal)
            if action == 2:
                situation.resoudre_situation(terminal)
            if action == 3:
                situation.analyser_resultats()
            if action == 4:
                situation.sauvegarder_situation("donnee")
            if action is None:
                break


def test():
    situation = Situation()
    situation.sauvegarder_situation("donnee")


def main():
    start_program()
    # test()


main()
