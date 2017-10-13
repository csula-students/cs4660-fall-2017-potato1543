"""
Searches module defines all different search algorithms
"""
import Queue as Q


def bfs(graph, initial_node, dest_node):
    """
    Breadth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
   
def dfs(graph, initial_node, dest_node):
    """
    Depth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    parents = {}
    dfs_recursion(graph, initial_node, {}, parents)
 
    path = []
    current_node = dest_node
    while current_node != initial_node:
        next_node = parents[current_node]
        path = [g.Edge(next_node, current_node, graph.distance(next_node, current_node))] + path
        current_node = next_node

    return path
 
def dfs_recursion(graph, current, discovered, parents):
     for neighbor in graph.neighbors(current):
         if neighbor in discovered:
             continue
         discovered[neighbor] = True
         parents[neighbor] = current
         dfs_recursion(graph, neighbor, discovered, parents)

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


