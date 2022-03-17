import pandas as pd
import networkx as nx

data = pd.read_csv('airports.csv')
G = nx.from_pandas_edgelist(data, source='Origin', target='Dest', edge_attr=True)

import matplotlib.pyplot as plt

plt.figure()
nx.draw_networkx(G, with_labels=True)
plt.show()

def dfs(start, end, path=None):
    if path is None:
        path = []

    if start in path:
        return None

    path.append(start)

    if start == end:
        return path

    start_nb = G.neighbors(start)
    end_nb = G.neighbors(end)

    for node in start_nb:
        if dfs(node, end, path):
            return path

    return None


def path_distance(start, end):
    path = dfs(start, end)
    return sum(G[node_a][node_b]['Distance'] for node_a, node_b in zip(path, path[1:]))

def path_air_time(start, end):
    path = dfs(start, end)
    return sum(G[node_a][node_b]['AirTime'] for node_a, node_b in zip(path, path[1:]))

print('Path from ISP to JAP', dfs('ISP', 'JAN'))
print('Distance from ISP to JAP', path_distance('ISP', 'JAN'))
print('Air time from ISP to JAP', path_air_time('ISP', 'JAN'))