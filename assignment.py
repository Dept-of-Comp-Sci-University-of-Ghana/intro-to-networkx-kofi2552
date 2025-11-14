import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

# Add nodes
members = ["Mensah", "Owusu", "Boateng", "Adjei", "Asare", "Koomson"]
G.add_nodes_from(members)

# Add edges with labels
relationships = [
    ("Mensah", "Owusu", "Admin oversight"),
    ("Mensah", "Boateng", "Admin oversight"),
    ("Owusu", "Boateng", "Collaboration"),
    ("Owusu", "Adjei", "Supervisor"),
    ("Boateng", "Asare", "Supervisor"),
    ("Owusu", "Koomson", "Supervisor"),
    ("Adjei", "Asare", "Collaboration"),
]

for a, b, label in relationships:
    G.add_edge(a, b, label=label)

# Draw
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=1000)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(a,b):lbl for a,b,lbl in relationships})
