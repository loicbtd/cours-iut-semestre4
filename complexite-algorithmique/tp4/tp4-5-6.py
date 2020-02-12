from networkx import *
import itertools as it
import random
import re
import matplotlib.pyplot as plt


def lire_graphe_depuis_fichier(nom_fichier):
    fichier = open(nom_fichier, "r")
    lignes = fichier.readlines()
    fichier.close()

    graphe = Graph()

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
    graphe = Graph()
    while len(graphe.nodes()) < 3:
        graphe = Graph()
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
    pos = kamada_kawai_layout(graphe, weight="weight")
    draw(graphe, pos, with_labels=True)
    labels = nx.get_edge_attributes(graphe, 'weight')
    draw_networkx_edge_labels(graphe, pos, edge_labels=labels)
    plt.show()


def imprimer_graphe(graphe):
    print(graphe.nodes())
    for sommet in graphe.edges():
        print(sommet, graphe.get_edge_data(sommet[0], sommet[1], ['weight']))


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


# def dijkstra(graphe, sommet_de_depart):



def main():
    graphe = lire_graphe_depuis_fichier("graphe-connexe.txt")

    # recuperer_matrice_plus_courtes_distances(graphe, 1)


    # dessiner_graphe(graphe)
    # graphe = generer_graphe_aleatoire()
    # imprimer_graphe(graphe)


main()

