import sys
import getopt
import networkx as nx


def creation_graphe_k_degenere_max(k,n):
    G = nx.Graph()
    if n == 0:
        return -1
    if n<=k+1:
        for i in range(1, n+1):
            G.add_node(i)
            if i>1:
                for j in range(i-1, 0, -1):
                    G.add_edge(i, j)
    else:
        for i in range(1, k+2):
            G.add_node(i)
            if i>1:
                for j in range(i-1, 0, -1):
                    G.add_edge(i, j)
        for i in range(k+2, n+1):
            G.add_node(i)
            for j in range(i-1, i-1-k,-1):
                G.add_edge(i, j)
    return G


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
        print("Options : \n\t-i\tnom du fichier contenant le graphe")
        print("\t-k\tvaleur de dégénérescence\n")
        print("\t-o\tnom de fichier pour écrire la suite de sommet à supprimer dans le cas où le graphe est k-dégénéré(par defaut : default.txt)")
        print("Exemple : python3 graphe.py -i graphe.txt -k 3")
        quit()

#-Fin options-#

if k==-1 or n==-1:
    print("Veuillez entrer ")


graphe_max = creation_graphe_k_degenere_max(k, n)
if graphe_max!=-1:
    print("Graphe ",k,"-degenere maximum copié dans ",output_filename,".")
    nx.write_adjlist(graphe_max, output_filename)