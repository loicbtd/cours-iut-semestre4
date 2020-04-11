import networkx as nx
from modele import BetterGraph as Bg
import random
import re
import matplotlib.pyplot as plt
import termcolor


def lire_graphe_depuis_fichier(chemin_absolu_fichier):
    fichier = open(chemin_absolu_fichier, "r")
    lignes = fichier.readlines()
    fichier.close()
    graphe = nx.Graph()
    for ligne in lignes:
        sommet = re.search(r'[^:]*', ligne).group()
        graphe.add_node(sommet)

        liste_aretes = re.findall(r'(\w*[(]\w*[)])', ligne)
        print(liste_aretes)
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
    for sommet in graphe.nodes():  # pour chaque sommet du graphe
        chemin = []
        chemin.append(sommet)  # l'ajouter à la liste du des sommets du chemin
        graphe_temporaire = graphe.copy()

        for (sommet_a, sommet_b) in graphe_temporaire.edges():  # pour les deux sommets reliés par chaque arete
            # si le dernier sommet du chemin est égal à l'un des deux sommets de l'arete, alors supprimmer l'arete
            if chemin[-1] == sommet_a:
                chemin.append(sommet_b)
                graphe_temporaire.remove_edge(sommet_a, sommet_b)

            elif chemin[-1] == sommet_b:
                chemin.append(sommet_a)
                graphe_temporaire.remove_edge(sommet_a, sommet_b)
            #  si la longueur du chemin est égal à au nombre de sommets du graphe, alors retourner vrai
            if len(chemin) == len(graphe.nodes()):
                return True
    return False  # à la fin, retourner faux


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


def calculer_total_poids_aretes(graphe, liste_sommets):
    poids_aretes_total = 0

    if len(liste_sommets) == 2:
        if liste_sommets[0] == liste_sommets[1]:
            return 0

    for i in range(0, len(liste_sommets) - 1, 1):
        if graphe.get_edge_data(liste_sommets[i], liste_sommets[i + 1], ['weight']) is None:
            poids_aretes_total += graphe.get_edge_data(liste_sommets[i], liste_sommets[i + 1], ['weight']).get('weight')
        else:
            poids_aretes_total += graphe.get_edge_data(liste_sommets[i + 1], liste_sommets[i], ['weight']).get('weight')
    return poids_aretes_total


def dijkstra(graphe, sommet_de_depart, sommet_de_fin):
    if str(sommet_de_depart) == str(sommet_de_fin):
        return [sommet_de_depart, sommet_de_fin]

    if (sommet_de_depart, sommet_de_fin) in graphe.edges() or (sommet_de_fin, sommet_de_depart) in graphe.edges():
        return [sommet_de_depart, sommet_de_fin]

    smallest = min(sommet_de_depart, sommet_de_fin)
    highest = max(sommet_de_depart, sommet_de_fin)

    bg_graphe = Bg.BetterGraph().copy_graph(graphe)
    sommet_choisi = smallest

    # Définir l'infini qui est ici égal à la somme du poids de toutes les arêtes + 1
    infini = 1
    for arete in bg_graphe.edges():
        infini += graphe.get_edge_data(arete[0], arete[1], ['weight']).get('weight')

    for sommet in bg_graphe.nodes():
        if sommet == smallest:
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

    # Inialisation du plus court chemin avec le sommet de fin
    plus_court_chemin = []
    plus_court_chemin.append(highest)

    # Recherche du plus court chemin en partant du sommet de fin
    while smallest not in plus_court_chemin:
        predecesseur = bg_graphe.get_node_property(plus_court_chemin[-1], 'predecesseur')
        # print("sommet de depart: ", smallest)
        # print("sommet de fin: ", highest)
        # print("ajout du sommet: ", plus_court_chemin)
        if predecesseur is not None:
            plus_court_chemin.append(predecesseur)

    # Inversion du plus court chemin pour le mettre dans le sens début vers fin
    if sommet_de_depart == smallest:
        plus_court_chemin = [plus_court_chemin[i] for i in range(len(plus_court_chemin) - 1, -1, -1)]

    # Trouver le poids total entre les aretes du plus court chemin
    poids_aretes_total = 0
    for i in range(0, len(plus_court_chemin) - 1, 1):
        poids_aretes_total += bg_graphe.get_edge_data(plus_court_chemin[i], plus_court_chemin[i + 1], ['weight']).get(
            'weight')

    return plus_court_chemin


def calculer_matrice_adjacence(graphe):
    matrice_adjacence = []
    for sommet1 in graphe.nodes():
        liste_adjacence = []
        for sommet2 in graphe.nodes():
            liste_adjacence.append(calculer_total_poids_aretes(graphe, dijkstra(graphe, sommet1, sommet2)))
        matrice_adjacence.append(liste_adjacence)
    return matrice_adjacence


def imprimer_matrice_adjacence(graphe):
    matrice_adjacence = calculer_matrice_adjacence(graphe)
    print(end='\t')
    for sommet in graphe.nodes():
        print(termcolor.colored(sommet, 'red'), end='\t')
    print()

    for i in range(len(matrice_adjacence)):
        print(termcolor.colored(list(graphe.nodes())[i], 'red'), end='\t')
        for j in range(len(matrice_adjacence)):
            print(matrice_adjacence[i][j], end='\t')
        print()


def calculer_longueur_tourner(graphe):
    return calculer_total_poids_aretes(graphe, dijkstra(graphe, graphe.nodes[0], graphe.nodes[-1])) + calculer_total_poids_aretes(graphe, [graphe.nodes[0], graphe.nodes[-1]])


# def main():
#     graphe = lire_graphe_depuis_fichier("graphe-connexe-longer.txt")
#     imprimer_matrice_adjacence(graphe)


# def creer_matrice_distance_old(graphe):
#     matrice = []
#     for i in range(len(graphe.nodes())):
#         ligne = []
#         for j in range(len(graphe.nodes())):
#             if (i, j) in graphe.edges() or (j, i) in graphe.edges():
#                 ligne.append(int(graphe.get_edge_data(i, j)['weight']))
#             else:
#                 ligne.append(0)
#         matrice.append(ligne)
#     return matrice
#
#
# def recuperer_matrice_plus_courtes_distances_old(graphe, sommet_de_depart):
#     # algorithme de Dijkstra
#     matrice_adjacence = creer_matrice_distance_old(graphe)
#
#     infini = sum(sum(ligne) for ligne in matrice_adjacence) + 1
#     nb_sommets = len(matrice_adjacence)
#
#     s_connu = {sommet_de_depart: [0, [sommet_de_depart]]}
#     s_inconnu = {k: [infini, ''] for k in range(nb_sommets) if k != sommet_de_depart}
#
#     for suivant in range(nb_sommets):
#         if matrice_adjacence[sommet_de_depart][suivant]:
#             s_inconnu[suivant] = [matrice_adjacence[sommet_de_depart][suivant], sommet_de_depart]
#
#     print('Dans le graphe d\'origine {} de matrice d\'adjacence : '.format(sommet_de_depart))
#     for ligne in matrice_adjacence:
#         print(ligne)
#     print()
#     print('Plus courts chemin de ')
#
#     while s_inconnu and any(s_inconnu[k][0] < infini for k in s_inconnu):
#
#         u = min(s_inconnu, key=s_inconnu.get)
#
#         longueur_u, precedent_u = s_inconnu[u]
#
#         for v in range(nb_sommets):
#             if matrice_adjacence[u][v] and v in s_inconnu:
#                 d = longueur_u + matrice_adjacence[u][v]
#                 if d < s_inconnu[v][0]:
#                     s_inconnu[v] = [d, u]
#         s_connu[u] = [longueur_u, s_connu[precedent_u][1] + [u]]
#         del s_inconnu[u]
#         print('longueur :', longueur_u, ':', ' -> '.join(map(str, s_connu[u][1])))
#
#     for k in s_inconnu:
#         print('Il n\'y a aucun chemin de {} a {}.'.format(sommet_de_depart, k))
#
#     return s_connu
