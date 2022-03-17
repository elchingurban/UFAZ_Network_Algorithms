from networkx.algorithms.shortest_paths import weighted
import pandas as pd
import networkx as nx

source = 2
destination = 1
weight = 'Kbps_AVG'
reversed_weight = '_Kbps_AVG'

data = pd.read_csv('sample_network.csv')
G = nx.from_pandas_edgelist(data, source='Source', target='Sink', edge_attr=True, create_using=nx.DiGraph)

def prepare_graph(G):
  for edge in G.edges():
    x1 = edge[0]
    x2 = edge[1]
    print(G.edges[x1, x2])

def dfs(G, source, destination):
  no_path = False
  cur_node = source
  path = [cur_node]
  unvisited = []
  for g in G:
    unvisited.append(g)

  while len(unvisited) != 0:
    do_continue = False

    if(cur_node == destination):
      break      
    
    for neighbor in list(G.neighbors(cur_node)):
      if(neighbor in unvisited):
        unvisited.remove(neighbor)
        path.append(neighbor)
        cur_node = neighbor
        do_continue = True
        break
    
    if(do_continue):
      continue
    
    path.pop()
    if(len(path) == 0):
      no_path = True
      break

    cur_node = path[len(path) - 1]
  
  if(no_path):
    return -1
  else:
    return path

def ford_fulkerson(G, source, destination):

  print(dfs(G, source, destination))

# ford_fulkerson(G, source, destination)

prepare_graph(G)

