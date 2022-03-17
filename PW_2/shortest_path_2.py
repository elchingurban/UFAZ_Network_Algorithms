import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

origin = 'Baku'
destiny = 'Imishli'

data = pd.read_csv('cities_in_az.csv')
G = nx.from_pandas_edgelist(data, source=data.columns[0], target=data.columns[1], edge_attr=True, create_using=nx.DiGraph)

print(nx.shortest_path(G, source=origin, target=destiny, weight='Hours'))