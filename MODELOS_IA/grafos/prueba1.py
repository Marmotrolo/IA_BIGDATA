import networkx as nx
import matplotlib.pyplot as plt

# 1. Crear un grafo no dirigido
G = nx.Graph()

# 2. Añadir nodos y aristas
G.add_edge('A', 'B')
G.add_edge('A', 'C')
G.add_edge('A', 'D')

# Para grafo dirigido (dígrafo), usa: G = nx.DiGraph()

# 3. Consultar datos básicos
print("Nodos:", G.nodes)
print("Aristas:", G.edges)

# 4. Dibujar el grafo
nx.draw(G, with_labels=True, node_color='lightblue', node_size=800)
plt.show()
