import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

origin = 'CRP'
destination = 'BOI'
weight = 'AirTime'

def djikstra(G, origin):
    dict = {}
    unvisited = []

    for node in G:
        dict.update({node: float('inf')})
        unvisited.append(node)
    dict.update({origin: 0})

    queue = [origin]

    while queue:
        node = queue.pop()

        if(node in unvisited):
            unvisited.remove(node)

        for neighbor in list(G.neighbors(node)):
            if(neighbor in unvisited):
                unvisited.index(neighbor)
                queue.append(neighbor)

            attr = G.edges[node, neighbor]

            old_value = dict[neighbor]
            new_value = dict[node] + attr[weight]
            if(new_value < old_value):
                dict.update({neighbor: new_value})
    
    return dict

data = pd.read_csv('airports.csv')
G = nx.from_pandas_edgelist(data, source=data.columns[9], target=data.columns[10], edge_attr=True, create_using=nx.DiGraph)

print(djikstra(G, origin)[destination])

plt.figure()
nx.draw_networkx(G, with_labels=True)
plt.show()
