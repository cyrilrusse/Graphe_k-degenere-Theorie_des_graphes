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
    
    copie_graphe = G.copy()
    while nbr_suppression:
        liste_noeud = list(copie_graphe.nodes)
        nbr_suppression = False
        for i in liste_noeud:
            if copie_graphe.degree[i]<=k:
                copie_graphe.remove_node(i)
                nbr_suppression = True
                liste_noeud_a_supprimer.append(i)
                break
    
    if copie_graphe.number_of_nodes()>0:
        print("Le graphe donné n'est pas",k,"dégénéré.")
        return False
    return liste_noeud_a_supprimer

def affichage_liste_noeud(nom_fichier, liste_noeud):
    fichier = open(nom_fichier, "w")
    for noeud in liste_noeud:
        fichier.write("{},".format(noeud))


#---FIN Fonction---#

#---Main---#
intput_filename = "0"
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
        print("Options : \n\t-i\tnom du fichier contenant le graphe")
        print("\t-k\tvaleur de dégénérescence\n")
        print("\t-o\tnom de fichier pour écrire la suite de sommet à supprimer dans le cas où le graphe est k-dégénéré(par defaut : default.txt)")
        print("Exemple : python3 graphe.py -i graphe.txt -k 3")
        quit()

if k==-1:
    print("Veuillez donner une valeur de k pour vérifier que votre graphe est k-dégénéré.")
    print("Utilisez l'option -h pour afficher l'aide.")
    quit()
#-Fin options-#

G = lecture_fichier(intput_filename)

liste = est_k_degenere(G, k)
if(liste != False):
    affichage_liste_noeud(output_filename, liste)
    print("La suite de noeud à supprimer a été copiée dans", output_filename,".")
