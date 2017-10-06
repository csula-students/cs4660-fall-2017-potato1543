"""
Searches module defines all different search algorithms
"""

def bfs(graph, initial_node, dest_node):
    """
    Breadth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    Q = []
    visited_nodes = []
    parent = {}
    nodes_distance = {}
    Q.append(initial_node)
    parent[initial_node] = None
    nodes_distance[initial_node] = 0
    visited_nodes.append(initial_node)
    while (!q is empty):
        current_node = Q.pop(0)
        for neighbor in graph.neighbors(current_node):
            if (neighbor not in visited_nodes):
                Q.append(neighbor)
                nodes_distance[neighbor] = nodes_distance[current_node] + graph.distance(current_node,neighbor)
                parent[neighbor] = current_node
                visited_nodes.append(neighbor)
         if (dest_node in visited_nodes):
             break
 
     list = []
     while parent[dest_node] is not None:
         list = [graph.get_edge(parent[dest_node],dest_node)]+ list
         dest_node = parent[dest_node]
 
     return list

def dfs(graph, initial_node, dest_node):
    """
    Depth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    if dest_node is None:
        dest_node = set()
    dest_node.add(initial_node)
    for next in graph[initial_node] - dest_node:
        dfs(graph,next, dest_node)
        return dest_node

def dijkstra_search(graph, initial_node, dest_node):
    """
    Dijkstra Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    pass

def a_star_search(graph, initial_node, dest_node):
    """
    A* Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    pass


# main method to see whats printing
