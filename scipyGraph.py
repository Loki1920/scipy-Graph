
import numpy as np
from scipy.sparse.csgraph import connected_components
from scipy.sparse.csgraph import dijkstra
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse.csgraph import bellman_ford
from scipy.sparse.csgraph import depth_first_order
from scipy.sparse.csgraph import breadth_first_order
from scipy.sparse import csr_matrix

arr = np.array([
  [0, 1, 2],
  [1, 0, 0],
  [2, 0, 0]
])

newarr = csr_matrix(arr)

print(connected_components(newarr))

#dijkstra : Find the shortest path from element 1 to 2:
print(dijkstra(newarr,return_predecessors= True,indices=0))

#Use the floyd_warshall() method to find shortest path between all pairs of elements.
print(floyd_warshall(newarr,return_predecessors= True))

# The bellman_ford() method can also find the shortest path between all pairs of elements, but this method can handle negative weights as well.
print(bellman_ford(newarr,return_predecessors= True,indices=0))

#Depth First Order:The depth_first_order() method returns a depth first traversal from node 
print(depth_first_order(newarr,1))

# Breadth First Order
#The breadth_first_order() method returns a breadth first traversal from a node.
print(breadth_first_order(newarr,1))