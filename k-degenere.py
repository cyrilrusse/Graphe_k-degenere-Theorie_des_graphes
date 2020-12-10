#---------------------------------------------------------#
#   Programme de vérification qu'un graphe est k-dégénéré
#   MATH0499 - Théorie des graphes
#   Projet(12) - graphe k-dégénéré
#   Randaxhe Martin - Russe Cyril
#---------------------------------------------------------#

import sys
import getopt
import networkx as nx


#---Fonction---#

def lecture_fichier(nom_fichier):
    G = nx.read_adjlist(nom_fichier)

    return G

def est_k_degenere(G, k):
    nbr_suppression = True
    liste_noeud_a_supprimer = []
    liste_a_supprimer = []

    copie_graphe = G.copy()
    while nbr_suppression:
        liste_a_supprimer.clear()
        liste_noeud = list(copie_graphe.nodes)
        liste_noeud.reverse()
        nbr_suppression = False
        for i in liste_noeud:
            if copie_graphe.degree[i]<=k:
                copie_graphe.remove_node(i)
                nbr_suppression = True
                liste_noeud_a_supprimer.append(i)
            
    if copie_graphe.number_of_nodes()>0:
        print("Le graphe donné n'est pas",k,"dégénéré.")
        return False
    print("Le graphe donné est",k,"dégénéré.")
    return liste_noeud_a_supprimer

def affichage_liste_noeud(nom_fichier, liste_noeud):
    fichier = open(nom_fichier, "w")
    for noeud in liste_noeud:
        fichier.write("{}\n".format(noeud))


#---FIN Fonctions---#

#---Main---#
intput_filename = False
output_filename = "default.txt"
k = -1

#-Gestion des options-#
options, remainder = getopt.getopt(sys.argv[1:], 'o:i:k:h', ['output=', 'input=','version=',])

for opt, arg in options:
    if opt == '-o':
        output_filename = arg
    elif opt == '-i':
        intput_filename = arg
    elif opt == '-k':
        k = int(arg)
    elif opt =='-h':
        print("Ce programme vérifie si le graphe donné en argument est k-dégénéré, si oui écrit dans un fichier une suite de noeud prouvant qu'il est k-dégénéré.\n")
        print("Options : \n\t-i\tNom du fichier contenant le graphe")
        print("\t-k\tValeur de dégénérescence\n")
        print("\t-o\tNom de fichier pour écrire la suite de sommet à supprimer dans le cas où le graphe est k-dégénéré(par defaut : default.txt)")
        print("\t-h\tAffichage de l'aide")
        print("Exemple : python3 graphe.py -i graphe.txt -k 3 [-o liste_sommet.txt]")
        quit()

if k==-1 or intput_filename==False:
    print("Veuillez donner la valeur de k-dégénérescence et le nom du fichier contenant le graphe.")
    print("Utilisez l'option -h pour afficher l'aide.")
    quit()
elif k<1 or k==0:
    print("Veuillez donner une valeur de k valide.")
    print("Utilisez l'option -h pour afficher l'aide.")
    quit()
#-Fin options-#

G = lecture_fichier(intput_filename)
liste = est_k_degenere(G, k)

if(liste != False):
    affichage_liste_noeud(output_filename, liste)
    print("La suite de noeud à supprimer a été copiée dans", output_filename,".")
