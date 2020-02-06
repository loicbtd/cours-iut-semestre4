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
    return is_connected(graphe)


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


def main():
    # graphe = lire_graphe_depuis_fichier("graph.txt")
    graphe = generer_graphe_aleatoire()

    print(est_connexe(graphe))

    imprimer_graphe(graphe)
    dessiner_graphe(graphe)


main()



# def est_complet(graphe):
#     if len(graphe.edge()) != len(graphe.nodes()) - 1:
#         return False
#     return True