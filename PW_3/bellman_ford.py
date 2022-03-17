import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

origin = 'CRP'
destination = 'BOI'
weight = 'AirTime'

def bellman_ford(G, origin):
    dict = {}

    num_of_nodes = 0
    for node in G:
        dict.update({node: float('inf')})
        num_of_nodes += 1
    dict.update({origin: 0})

    for i in range(0, num_of_nodes-1):
        for node in G:
            for neighbor in list(G.neighbors(node)):
                attr = G.edges[node, neighbor]

                old_value = dict[neighbor]
                new_value = dict[node] + attr[weight]

                if(new_value < old_value):
                    dict.update({neighbor: new_value})
    
    return dict

data = pd.read_csv('airports.csv')
G = nx.from_pandas_edgelist(data, source=data.columns[9], target=data.columns[10], edge_attr=True, create_using=nx.DiGraph)

print(bellman_ford(G, origin)[destination])

plt.figure()
nx.draw_networkx(G, with_labels=True)
plt.show()
