"""
Searches module defines all different search algorithms
"""
import Queue as Q
import graph as G

def bfs(graph, initial_node, dest_node):
    """
    Breadth First Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    distance_of = {}
    parent_of = {}
    edge_to = {}

    q = []
    q.append((0, initial_node));

    distance_of[initial_node] = 0

    while len(q) > 0:
        u = q.pop()[1]

        for node in graph.neighbors(u):
            if node not in distance_of:
                edge_to[node] = graph.distance(u, node)
                distance_of[node] = distance_of[u] + edge_to[node].weight
                parent_of[node] = u

                # continue to enqueue if we haven't reached the end
                if node != dest_node:
                    q.append((distance_of[node], node))

        # sort priority
        q = sorted(q, key=lambda x:x[0])
        q.reverse()

    # actions is a list of edges
    actions = []
    end_node = dest_node

    while end_node in parent_of:
        actions.append(edge_to[end_node])
        end_node = parent_of[end_node]

    # reverse the list of edges
    actions.reverse()

    return actions



   
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
        path = [G.edge(next_node, current_node, graph.distance(next_node, current_node))] + path
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
    distance_of = {}
    previous_of = {}
    edge_to = {}

    distance_of[initial_node] = 0

    q = []
    q.append((0, initial_node))

    while len(q) > 0:
        u = q.pop()[1]

        for v in graph.neighbors(u):
            edge = graph.distance(u, v)
            alt = distance_of[u] + edge.weight

            if v not in distance_of or alt < distance_of[v]:
                # reassign priority
                if v in distance_of:
                    q.remove((distance_of[v], v))
                # enqueue v for further evaluations
                q.append((alt, v))

                distance_of[v] = alt
                previous_of[v] = u
                edge_to[v] = edge

        # sort priority
        q = sorted(q, key=lambda x:x[0])
        q.reverse()
    
    actions = []
    current_node = dest_node

    while current_node in previous_of:
        actions.append(edge_to[current_node])
        current_node = previous_of[current_node]

    actions.reverse()

    return actions


def a_star_search(graph, initial_node, dest_node):
    """
    A* Search
    uses graph to do search from the initial_node to dest_node
    returns a list of actions going from the initial node to dest_node
    """
    pass


