#--------------------------------------------------------#
#   Programme de création de graphe k-dégénéré maximaux
#   MATH0499 - Théorie des graphes
#   Projet(12) - graphe k-dégénéré
#   Randaxhe Martin - Russe Cyril
#--------------------------------------------------------#

import sys
import getopt
import networkx as nx

#---Fonctions---#
def creation_graphe_k_degenere_max(k,n):
    G = nx.Graph()
    if n <= 0:
        print("Votre graphe doit avoir au min 1 noeud.")
        return -1

    if k>=n:
        min = n+1
    else:
        min = k+2
    #premiers noeuds allant jusqu'au plus k+1 qui doivent tous être reliés entre eux
    for i in range(1, min):
        G.add_node(i)
        if i>1:
            for j in range(i-1, 0, -1):
                G.add_edge(i, j)
    #noeuds suivants jusque n étant, eux, reliés aux k éléments précédents
    if min == k+2:
        for i in range(k+2, n+1):
            G.add_node(i)
            for j in range(i-1, i-1-k,-1):
                G.add_edge(i, j)
    return G
#---Fin Fonctions---#

#---Main---#
output_filename = "k-degenere_max.txt"
k = -1
n = -1

#-Gestion des options-#
options, remainder = getopt.getopt(sys.argv[1:], 'o:n:k:h', ['output=', 'input=','version=',])

for opt, arg in options:
    if opt == '-o':
        output_filename = arg
    elif opt == '-n':
        n = int(arg)
    elif opt == '-k':
        k = int(arg)
    elif opt =='-h':
        print("Options : \n\t-o\tNom du fichier dans lequel écrire le graphe k-dégénéré max (.txt) (par défaut : k-degenere_max.txt)")
        print("\t-k\tValeur de dégénérescence\n")
        print("\t-n\tNombre de noeud voulu pour le graphe k-dégénéré max à créer")
        print("\t-h\tAffichage de l'aide")        
        print("Exemple : python3 k-degenere_max.py [-o graphe.txt] -k 3 -n 6")
        quit()

#-Fin options-#

if k==-1 or n==-1:
    print("Veuillez entrer une valeur de k et de n avec les options correspondantes.")
    quit()


graphe_max = creation_graphe_k_degenere_max(k, n)
if graphe_max!=-1:
    print("Graphe ",k,"-degenere maximum copié dans ",output_filename,".")
    nx.write_adjlist(graphe_max, output_filename)