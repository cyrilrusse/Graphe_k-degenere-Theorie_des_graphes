import matplotlib.pyplot as plt

import networkx as nx


#---Fonction---#

def lecture_fichier(nom):
    
    



print("Veuillez entrez un nom de fichier : ")
nom_fichier = input()

fichier = open(nom_fichier, "r")

texte = fichier.readline()

print(texte)

G = nx.Graph()

G.add_node(1)
G.add_node(2)


G.add_edge(1,2)

print(G.number_of_edges())

plt.subplot(121)

nx.draw(G, with_labels=True, font_weight='bold')

plt.show()
