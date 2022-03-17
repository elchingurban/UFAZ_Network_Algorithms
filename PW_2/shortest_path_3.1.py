import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

origin = 'Baku'
destiny = 'Imishli'

data = pd.read_csv('cities_in_az.csv')
G = nx.from_pandas_edgelist(data, source=data.columns[0], target=data.columns[1], edge_attr=True, create_using=nx.DiGraph)

plt.figure()
nx.draw_networkx(G, with_labels=True)
plt.show()

print(nx.shortest_path(G, source=origin, target=destiny, weight='Hours'))

nx.add_path(G, ['Baku', 'Imishli'])
G.edges['Baku', 'Imishli']['Hours'] = 1.29

print(nx.shortest_path(G, source=origin, target=destiny, weight='Hours'))

# The difference between those 2 pathes is that after adding the direct path from Baku to Imishli its considered as the new shortest path
print('-----------------------------')

print(nx.shortest_path(G, source=origin, target=destiny, weight='Hours'))
print(nx.shortest_path(G, source=destiny, target=origin, weight='Hours'))

# Since our graph is directional, the path used for getting to Imishli from Baku can't be used for getting back