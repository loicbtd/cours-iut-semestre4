import signal
import vue.Terminal as Terminal
import modele.Traitements as Traitements

menu_graphe = ("Menu Graphe",
               "Choisissez une action: ",
               {'1': 'Dessiner le graphe',
                '2': 'Afficher la matrice des distances entre toutes le villes du graphe (matrice d\'adjacence)',
                '3': 'Calculer la longueur d\'une tournée'},
               "Retour")

menu_principal = ("Menu Principal",
                  "Choisissez une action:",
                  {'1': 'Charger un graphe à partir d\'un fichier',
                   '2': 'Générer aléatoirement un graphe connexe'},
                  "Quitter")


def traiter_signal(signal_recu, traitement):
    print()
    exit(0)


def start_program():
    signal.signal(signal.SIGINT, traiter_signal)

    terminal = Terminal.Terminal("Projet : Problème du voyageur de commerce")

    terminal.imprimer_message("\t\t\t\tBienvenue !\n\n\n\n\t\t\t® Loïc BERTRAND - 2020  ", 0)

    while True:
        action = terminal.choisir_dans_menu(menu_principal)
        if action == 1:
            chemin_fichier = terminal.choisir_fichier_dans_dossier("donnee")
            if chemin_fichier is None:
                continue
            graphe = Traitements.lire_graphe_depuis_fichier(chemin_fichier)
        if action == 2:
            graphe = Traitements.generer_graphe_aleatoire()
        if action is None:
            break

        while True:
            action = terminal.choisir_dans_menu(menu_graphe)
            if action == 1:
                terminal.nettoyer()
                Traitements.dessiner_graphe(graphe)
                input()
            if action == 2:
                terminal.nettoyer()
                Traitements.imprimer_matrice_adjacence(graphe)
                input()
            if action == 3:
                terminal.nettoyer()
                print("Longueur d'une tournée: ", Traitements.calculer_longueur_tourner(graphe))
                input()
            if action is None:
                break

    terminal.nettoyer()


def main():
    start_program()


main()
