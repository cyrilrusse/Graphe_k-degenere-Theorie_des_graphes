import matplotlib.pyplot as plt
import networkx as nx

#affichage graphe

graphe = nx.read_adjlist("k-degenere_max.txt")


nx.draw(graphe, with_labels=True, font_weight='bold')
plt.show()