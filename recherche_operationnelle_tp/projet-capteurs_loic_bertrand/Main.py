from modele.Situation import *
import signal

menu_principal = ("Menu Principal",
                  "Choisissez une action:",
                  {'1': 'Créer manuellement une situation',
                   '2': 'Charger une situation à partir d\'un fichier'},
                  "Quitter")

menu_situation = ("Menu Situation",
                  "Choisissez une action: ",
                  {'1': 'Traiter la situation',
                   '2': 'Examiner l\'influence du nombre et du type des configurations',
                   '3': 'Sauvegarder la situation'},
                  "Retour")


def traiter_signal(signal_recu, traitement):
    print()
    exit(0)


def start_program():
    signal.signal(signal.SIGINT, traiter_signal)

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

        while True:
            action = terminal.choisir_dans_menu(menu_situation)
            if action == 1:
                situation.traiter_la_situation(terminal)
            if action == 2:
                situation.imprimer_situation(terminal)
                situation.examiner_influence_choix_situation()
            if action == 3:
                situation.sauvegarder_situation("donnee")
            if action is None:
                break
    terminal.nettoyer()


def main():
    start_program()


main()
