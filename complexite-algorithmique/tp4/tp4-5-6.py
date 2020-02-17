import networkx as nx
import BetterGraph as Bg
import itertools as it
import random
import re
import matplotlib.pyplot as plt


def lire_graphe_depuis_fichier(nom_fichier):
    fichier = open(nom_fichier, "r")
    lignes = fichier.readlines()
    fichier.close()
    graphe = nx.Graph()
    for ligne in lignes:
        sommet = re.search(r'[^:]*', ligne).group()
        graphe.add_node(sommet)

        liste_aretes = re.findall(r'(\w*[(]\w*[)])', ligne)
        for arete in liste_aretes:
            proprietes_arete = re.findall(r'([^()]+)', arete)
            sommet_voisin = proprietes_arete[0]
            poids = int(proprietes_arete[1])
            graphe.add_edge(sommet, sommet_voisin, weight=poids)
    return graphe


def generer_graphe_aleatoire():
    graphe = nx.Graph()
    while len(graphe.nodes()) < 3:
        graphe = nx.Graph()
        random.seed()
        taille_graohe = random.randint(0, 10)
        for sommet in range(0, taille_graohe):
            graphe.add_node(str(sommet))
            for sommet_voisin in range(0, taille_graohe):
                est_vrai = bool(random.getrandbits(1))
                if est_vrai:
                    if (sommet, sommet_voisin) not in graphe.edges() and (sommet_voisin, sommet) not in graphe.edges:
                        graphe.add_edge(str(sommet), str(sommet_voisin), weight=random.randint(0, 100))
    return graphe


def est_connexe(graphe):
    for sommet in graphe.nodes():
        chemin = []
        chemin.append(sommet)
        graphe_temporaire = graphe.copy()

        for (sommet_a, sommet_b) in graphe_temporaire.edges():

            if chemin[-1] == sommet_a:
                chemin.append(sommet_b)
                graphe_temporaire.remove_edge(sommet_a, sommet_b)

            elif chemin[-1] == sommet_b:
                chemin.append(sommet_a)
                graphe_temporaire.remove_edge(sommet_a, sommet_b)

            if len(chemin) == len(graphe.nodes()):
                return True
    return False


def dessiner_graphe(graphe):
    pos = nx.kamada_kawai_layout(graphe, weight="weight")
    nx.draw(graphe, pos, with_labels=True)
    labels = nx.get_edge_attributes(graphe, 'weight')
    nx.draw_networkx_edge_labels(graphe, pos, edge_labels=labels)
    plt.show()


def imprimer_graphe(graphe):
    print(graphe.nodes())
    for arete in graphe.edges():
        print(arete, graphe.get_edge_data(arete[0], arete[1], ['weight']))


def creer_matrice_distance_old(graphe):
    matrice = []
    for i in range(len(graphe.nodes())):
        ligne = []
        for j in range(len(graphe.nodes())):
            if (i, j) in graphe.edges() or (j, i) in graphe.edges():
                ligne.append(int(graphe.get_edge_data(i, j)['weight']))
            else:
                ligne.append(0)
        matrice.append(ligne)
    return matrice


def recuperer_matrice_plus_courtes_distances_old(graphe, sommet_de_depart):
    # algorithme de Dijkstra
    matrice_adjacence = creer_matrice_distance_old(graphe)

    infini = sum(sum(ligne) for ligne in matrice_adjacence) + 1
    nb_sommets = len(matrice_adjacence)

    s_connu = {sommet_de_depart: [0, [sommet_de_depart]]}
    s_inconnu = {k: [infini, ''] for k in range(nb_sommets) if k != sommet_de_depart}

    for suivant in range(nb_sommets):
        if matrice_adjacence[sommet_de_depart][suivant]:
            s_inconnu[suivant] = [matrice_adjacence[sommet_de_depart][suivant], sommet_de_depart]

    print('Dans le graphe d\'origine {} de matrice d\'adjacence : '.format(sommet_de_depart))
    for ligne in matrice_adjacence:
        print(ligne)
    print()
    print('Plus courts chemin de ')

    while s_inconnu and any(s_inconnu[k][0] < infini for k in s_inconnu):

        u = min(s_inconnu, key=s_inconnu.get)

        longueur_u, precedent_u = s_inconnu[u]

        for v in range(nb_sommets):
            if matrice_adjacence[u][v] and v in s_inconnu:
                d = longueur_u + matrice_adjacence[u][v]
                if d < s_inconnu[v][0]:
                    s_inconnu[v] = [d, u]
        s_connu[u] = [longueur_u, s_connu[precedent_u][1] + [u]]
        del s_inconnu[u]
        print('longueur :', longueur_u, ':', ' -> '.join(map(str, s_connu[u][1])))

    for k in s_inconnu:
        print('Il n\'y a aucun chemin de {} a {}.'.format(sommet_de_depart, k))

    return s_connu


def dijkstra(graphe, sommet_de_depart):
    bg_graphe = Bg.BetterGraph().copy_graph(graphe)
    sommet_choisi = sommet_de_depart

    # Définir l'infini qui est ici égal à la somme du poids de toutes les arêtes
    infini = 1
    for arete in bg_graphe.edges():
        infini += graphe.get_edge_data(arete[0], arete[1], ['weight']).get('weight')

    for sommet in bg_graphe.nodes():
        if sommet == sommet_de_depart:
            bg_graphe.set_node_property(sommet, 'marque', 'oui')
            bg_graphe.set_node_property(sommet, 'valeur', 0)
        else:
            bg_graphe.set_node_property(sommet, 'marque', 'non')
            bg_graphe.set_node_property(sommet, 'valeur', infini)

    # Tant qu'il existe un sommet non marqué
    presence_sommet_non_marque = True
    while presence_sommet_non_marque:

        # récupérer les voisins non marqués du sommet choisi
        voisins_sommet_choisi = []
        for arete in bg_graphe.edges():
            (sommet_a, sommet_b) = arete
            if sommet_a == sommet_choisi:
                if bg_graphe.get_node_property(sommet_b, 'marque') == 'non':
                    voisins_sommet_choisi.append(sommet_b)
            if sommet_b == sommet_choisi:
                if bg_graphe.get_node_property(sommet_a, 'marque') == 'non':
                    voisins_sommet_choisi.append(sommet_a)

        # Pour chaque sommet non marqué voisin du sommet choisi
        for sommet_voisin in voisins_sommet_choisi:
            valeur_sommet_voisin = bg_graphe.get_node_property(sommet_voisin, 'valeur')
            valeur_sommet_choisi = bg_graphe.get_node_property(sommet_choisi, 'valeur')
            valeur_arete = bg_graphe.get_edge_data(sommet_choisi, sommet_voisin, ['weight']).get('weight')
            nouvelle_valeur_sommet_voisin = min(valeur_sommet_voisin, valeur_sommet_choisi + valeur_arete)
            if nouvelle_valeur_sommet_voisin == valeur_sommet_choisi + valeur_arete:
                bg_graphe.set_node_property(sommet_voisin, 'predecesseur', sommet_choisi)
            bg_graphe.set_node_property(sommet_voisin, 'valeur', nouvelle_valeur_sommet_voisin)

        # Choisir le sommet non marqué de plus petit label
        sommet_choisi = min(bg_graphe.get_all_nodes_with_property('marque', 'non'))

        # Marquer le sommet choisi
        bg_graphe.set_node_property(sommet_choisi, 'marque', 'oui')

        # Tester s'il existe un sommet non marqué
        presence_sommet_non_marque = False
        for sommet in bg_graphe.nodes():
            if bg_graphe.get_node_property(sommet, 'marque') == 'non':
                presence_sommet_non_marque = True

    # Initialisation du sommet de fin avec un des sommets du graphe ayant un prédécesseur
    sommet_de_fin = 0
    for sommet in bg_graphe.nodes():
        if bg_graphe.get_node_property(sommet, 'predecesseur') is not None:
            sommet_de_fin = sommet
            break

    # Rercherche du sommet de fin du graphe (celui avec le plus grand prédécesseur)
    for sommet in bg_graphe.nodes():
        if bg_graphe.get_node_property(sommet, 'predecesseur') is not None:
            if bg_graphe.get_node_property(sommet, 'predecesseur') > bg_graphe.get_node_property(sommet_de_fin,
                                                                                                 'predecesseur'):
                sommet_de_fin = sommet

    # Inialisation du plus court chemin avec le sommet de fin
    plus_court_chemin = []
    plus_court_chemin.append(sommet_de_fin)

    # Recherche du plus court chemin en partant du sommet de fin
    while sommet_de_depart not in plus_court_chemin:
        predecesseur = bg_graphe.get_node_property(plus_court_chemin[-1], 'predecesseur')
        if predecesseur is not None:
            plus_court_chemin.append(predecesseur)
            print("ajout du sommet: ", predecesseur)

    # Inversion du plus court chemin pour le mettre dans le sens début vers fin
    plus_court_chemin = [plus_court_chemin[i] for i in range(len(plus_court_chemin) - 1, -1, -1)]

    # Trouver le poids total entre les aretes du plus court chemin
    poids_aretes_total = 0
    for i in range(0, len(plus_court_chemin) - 1, 1):
        poids_aretes_total += bg_graphe.get_edge_data(plus_court_chemin[i], plus_court_chemin[i+1], ['weight']).get('weight')

    return plus_court_chemin, poids_aretes_total


def main():
    graphe = lire_graphe_depuis_fichier("graphe-connexe.txt")

    # meilleur_graphe = BG.BetterGraph().copy_graph(graphe)

    (liste, poids) = dijkstra(graphe, '1')

    print(liste)
    print(poids)

    dessiner_graphe(graphe)


main()
