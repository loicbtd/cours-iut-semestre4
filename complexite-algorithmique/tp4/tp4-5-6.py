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
        noeud = re.search(r'[^:]*', ligne).group()
        graphe.add_node(noeud)

        liste_aretes = re.findall(r'(\w*[(]\w*[)])', ligne)
        for arete in liste_aretes:
            proprietes_arete = re.findall(r'([^()]+)', arete)
            noeud_voisin = proprietes_arete[0]
            poids = int(proprietes_arete[1])
            graphe.add_edge(noeud, noeud_voisin, weight=poids)

    return graphe


def generer_graphe_aleatoire():
    graphe = Graph()
    while len(graphe.nodes()) < 3:
        graphe = Graph()
        random.seed()
        taille_graohe = random.randint(0, 10)
        for noeud in range(0, taille_graohe):
            graphe.add_node(str(noeud))
            for noeud_voisin in range(0, taille_graohe):
                est_vrai = bool(random.getrandbits(1))
                if est_vrai:
                    if (noeud, noeud_voisin) not in graphe.edges() and (noeud_voisin, noeud) not in graphe.edges:
                        graphe.add_edge(str(noeud), str(noeud_voisin), weight=random.randint(0, 100))
    return graphe


def est_connexe(graphe):
    if len(graphe.nodes()) <= len(graphe.edges()) - 1:
        return False

    noeuds_provisoirement_marques = Graph()
    noeuds_marques = Graph()

    for noeud in graphe.nodes():
        noeuds_provisoirement_marques.add_node(noeud)
        break

    while len(noeuds_provisoirement_marques.nodes()) > 0:
        for noeud_selectionne in noeuds_provisoirement_marques.nodes():
            noeud = noeud_selectionne
            break
        for arete in graphe.edges():
            (noeud_a, noeud_b) = arete
            if arete == noeud_a:
                noeuds_provisoirement_marques.add_node(noeud_b)
            if arete == noeud_b:
                noeuds_provisoirement_marques.add_node(noeud_a)
        noeuds_provisoirement_marques.remove_node(noeud)
        noeuds_marques.add_node(noeud)

    print(noeuds_marques.nodes())
    if set(noeuds_marques.nodes()) <= set(graphe.nodes()):
        return True

    return False

def

def connexe(A):
    retour = False
    compteur = 0
    for node in A.nodes():
        for (a, b) in A.edges():
            compteur += 1
            # print(a,b,node)
            if a != node and b != node:
                retour = False
            else:
                retour = True

            if retour:
                break
            else:
                if compteur == len(A.edges()):
                    return False
                else:
                    continue
        compteur = 0
    return True

    # for noeud in graphe.nodes():
    #     graphe_tmp = graphe
    #     chemin = []
    #
    #     chemin.append(noeud)
    #
    #     for arete in graphe_tmp.edges():
    #
    #         (sommet_a, sommet_b) = arete
    #
    #         if chemin[-1] == sommet_a:
    #             chemin.append(sommet_b)
    #             # graphe_tmp.remove_edge(sommet_a, sommet_b)
    #             print(chemin)
    #
    #             break
    #         if chemin[-1] == sommet_b:
    #             chemin.append(sommet_a)
    #             # graphe_tmp.remove_edge(sommet_b, sommet_a)
    #             print(chemin)
    #             break
    #         # print(graphe.nodes)
    #         # print(graphe.edges)
    #         print(chemin)
    #         return False
    # return True


def dessiner_graphe(graphe):
    pos = kamada_kawai_layout(graphe, weight="weight")
    draw(graphe, pos, with_labels=True)
    labels = nx.get_edge_attributes(graphe, 'weight')
    draw_networkx_edge_labels(graphe, pos, edge_labels=labels)
    plt.show()


def imprimer_graphe(graphe):
    print(graphe.nodes())
    for noeud in graphe.edges():
        print(noeud, graphe.get_edge_data(noeud[0], noeud[1], ['weight']))


def creer_matrice_distance(graphe):
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


def recuperer_plus_courtes_distances(graphe, sommet_de_depart):
    # algorithme de Dijkstra
    matAdjacence = creer_matrice_distance(graphe)

    infini = sum(sum(ligne) for ligne in matAdjacence) + 1
    nb_sommets = len(matAdjacence)

    s_connu = {sommet_de_depart: [0, [sommet_de_depart]]}
    s_inconnu = {k: [infini, ''] for k in range(nb_sommets) if k != sommet_de_depart}

    for suivant in range(nb_sommets):
        if matAdjacence[sommet_de_depart][suivant]:
            s_inconnu[suivant] = [matAdjacence[sommet_de_depart][suivant], sommet_de_depart]

    print('Dans le graphe d\'origine {} de matrice d\'adjacence : '.format(sommet_de_depart))
    for ligne in matAdjacence:
        print(ligne)
    print()
    print('Plus courts chemin de ')

    while s_inconnu and any(s_inconnu[k][0] < infini for k in s_inconnu):

        u = min(s_inconnu, key=s_inconnu.get)

        longueur_u, precedent_u = s_inconnu[u]

        for v in range(nb_sommets):
            if matAdjacence[u][v] and v in s_inconnu:
                d = longueur_u + matAdjacence[u][v]
                if d < s_inconnu[u][0]:
                    s_inconnu[v] = [d, u]
        s_connu[u] = [longueur_u, s_connu[precedent_u][1] + [u]]
        del s_inconnu[u]
        print('longueur :', longueur_u, ':', ' -> '.join(map(str, s_connu[u][1])))

    for k in s_inconnu:
        print('Il n\'y a aucun chemin de {} a {}.'.format(sommet_de_depart, k))

    return s_connu


def main():
    graphe = lire_graphe_depuis_fichier("graphe-non-connexe.txt")
    # graphe = generer_graphe_aleatoire()

    imprimer_graphe(graphe)
    dessiner_graphe(graphe)

    print(est_connexe(graphe))


main()

# def est_complet(graphe):
#     if len(graphe.edge()) != len(graphe.nodes()) - 1:
#         return False
#     return True
