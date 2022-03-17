import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

origin = 'CRP'
destiny = 'BOI'

data = pd.read_csv('airports.csv')
G = nx.from_pandas_edgelist(data, source=data.columns[9], target=data.columns[10], edge_attr=True, create_using=nx.DiGraph)

print(nx.shortest_path(G, source=origin, target=destiny, weight='Distance'))

print(nx.shortest_path(G, source=origin, target=destiny, weight='AirTime'))

print('----------------------------------')

print('Connectivity degree')
print(G.degree(origin))
print(G.in_degree(origin))
print(G.out_degree(origin))

print('----------------------------------')

print('Closeness Centrality')
print('AirTime')
sum = 0.0
k = 0
for i in G:
    sum += len(nx.shortest_path(G, source=origin, target=i, weight='AirTime'))
    k += 1
print(sum/k)

print('Distance')
sum = 0.0
k = 0
for i in G:
    sum += len(nx.shortest_path(G, source=origin, target=i, weight='Distance'))
    k += 1
print(sum/k)

print('----------------------------------')

print('Betweenness Centrality')
print('AirTime')
node = 'TPA'
k = 0
for i in G:
    for j in G:
        if(node in nx.shortest_path(G, source=i, target=j, weight='AirTime')):
            k += 1
print(k)

print('Distance')
node = 'TPA'
k = 0
for i in G:
    for j in G:
        if(node in nx.shortest_path(G, source=i, target=j, weight='Distance')):
            k += 1
print(k)

print('----------------------------------')

print('Network Density')
sum = 0
k = 0
for i in G:
    sum += G.degree(i)
    k += 1
sum = sum / (k*(k-1))
print(sum)

print('----------------------------------')

print('Network Diameter')
print('Airtime')
max = len(nx.shortest_path(G, source=origin, target=destiny, weight='AirTime'))
for i in G:
    for j in G:
        l = len(nx.shortest_path(G, source=i, target=j, weight='AirTime'))
        if(max < l):
            max = l
print(l)

print('Distance')
max = len(nx.shortest_path(G, source=origin, target=destiny, weight='Distance'))
for i in G:
    for j in G:
        l = len(nx.shortest_path(G, source=i, target=j, weight='Distance'))
        if(max < l):
            max = l
print(l)

print('----------------------------------')
print('Network Average Path Length')
print('Airtime')
sum = 0
k = 0
for i in G:
    for j in G:
        sum += len(nx.shortest_path(G, source=i, target=j, weight='AirTime'))
        k += 1
print(sum/k)

print('Distance')
sum = 0
k = 0
for i in G:
    for j in G:
        sum += len(nx.shortest_path(G, source=i, target=j, weight='Distance'))
        k += 1
print(sum/k)