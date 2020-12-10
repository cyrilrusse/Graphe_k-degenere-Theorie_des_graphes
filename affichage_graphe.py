#------------------------------------#
#   Programe d'affichage de graphe
#   MATH0499 - Théorie des graphes
#   Projet(12) - graphe k-dégénéré
#   Randaxhe Martin - Russe Cyril
#------------------------------------#

import sys
import getopt
import matplotlib.pyplot as plt
import networkx as nx

intput_filename = False
#-Gestion des options-#
options, remainder = getopt.getopt(sys.argv[1:], 'i:h', ['output=', 'input=','version=',])

for opt, arg in options:
    if opt == '-i':
        intput_filename = arg
    elif opt =='-h':
        print("Options : \n\t-i\tnom du fichier contenant le graphe")
        print("\t-h\taffichage de l'aide")
        print("Exemple : python3 graphe.py -i graphe.txt")
        quit()

#-Fin options-#

if intput_filename==False:
    print("Veuillez entrer le nom de fichier contenant le graphe que vous voulez afficher avec l'option -i.")
    quit()


graphe = nx.read_adjlist(intput_filename)

nx.draw(graphe, with_labels=True, font_weight='bold')
plt.show()