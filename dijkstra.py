#!/usr/bin/python

# Dijkstra - Find the shortest path from vertex 1 to vertex N
# Dtra's algorithm. It picks the unvisited vertex with the lowest-distance,
# calculates the distance through it to each unvisited neighbor, and updates the
# neighbor's distance if smaller. Mark visited (set to red) when done with
# neighbors.
# Given an undirected graph G having positive weights and N vertices

def dijkstra(adj, src):
    """Dijkstra shortest path.
    Args:
      adj: adjacency matrix (symmetric) to represent a graph
           [[dist_00, dist_01, ..., dist_0,N-1],
            [dist_10, dist_11, ..., dist_1,N-1 ],
            ...
            [dist_N-1,0, ...,       dist_N-1,N-1]]

      src: src vertex
    """
    # use md[j] to record the current shortest distance from src vertex to
    # vertex j

    num_vertex = len(adj)

    md = num_vertex * [float("inf")]
    md[src] = 0
    unvisited = set(range(num_vertex))
    print("original unvisited %s" % unvisited)
    while len(unvisited) > 0:
      # find unvisited vertex of shortest distance
      k = nearest_neighbor(unvisited, md)
      print("nearest unvisited neighbor %s, unvisited set %s" % (k, unvisited))
      unvisited.remove(k)

      for v in unvisited:
        md[v] = min(adj[k][v] + md[k], md[v])

    return md

def nearest_neighbor(unvisited, md):
  index = None
  min_val = None
  for k in unvisited:
    if min_val == None:
      index = k
      min_val = md[k]
    elif md[k] < min_val:
      index = k
  return index


if __name__ == "__main__":
  x = float("inf")
  adj = [[0,1,1,x,x],
         [1,0,x,2,x],
         [1,x,0,1,4],
         [x,2,1,0,1],
         [x,x,4,1,0]]
  print(adj)
  src = 0
  dst = 4
  md = dijkstra(adj,0)
  print(md)
  print(md[dst])

