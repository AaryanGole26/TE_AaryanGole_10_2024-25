def aStarAlgo(start_node, stop_node):
    open_set = {start_node}  # Initialize open set with start_node
    closed_set = set()
    g = {}  # Store distance from starting node
    parents = {}  # Parents contains an adjacency map of all nodes

    # Distance of starting node from itself is zero
    g[start_node] = 0
    # Start_node is root node, so start_node is set to its own parent
    parents[start_node] = start_node

    while len(open_set) > 0:
        n = None

        # Node with the lowest f() is found
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n is None:
            print('Path does not exist!')
            return None

        # If the current node is the stop_node, we reconstruct the path
        if n == stop_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()

            print('Path found: {}'.format(path))
            return path

        # Get neighbors of the current node
        neighbors = get_neighbors(n)
        if neighbors is not None:
            for (m, weight) in neighbors:
                # Nodes 'm' not in open_set and closed_set are added to open_set
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight
                else:
                    # For each node m, compare its distance from start with the distance through n
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        # If m is in closed_set, move it back to open_set
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)

        # Move n from open_set to closed_set after all neighbors are checked
        open_set.remove(n)
        closed_set.add(n)

    print('Path does not exist!')
    return None

# Define function to return neighbor and its distance
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None

# Heuristic function to return heuristic distance for all nodes
def heuristic(n):
    H_dist = {
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0,
    }
    return H_dist[n]

# Describe your graph here  
Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': None,
    'E': [('D', 6)],
    'D': [('G', 1)],
}

aStarAlgo('A', 'G')

''' 
Output : 
 Path found: ['A', 'E', 'D', 'G']
'''
