"""
utils package is for some quick utility methods

such as parsing
"""
#import edge
#import node
import graph

class Tile(object):
    """Node represents basic unit of graph"""
    def __init__(self, x, y, symbol):
        self.x = x
        self.y = y
        self.symbol = symbol

    def __str__(self):
        return 'Tile(x: {}, y: {}, symbol: {})'.format(self.x, self.y, self.symbol)
    def __repr__(self):
        return 'Tile(x: {}, y: {}, symbol: {})'.format(self.x, self.y, self.symbol)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y and self.symbol == other.symbol
        return False
    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(str(self.x) + "," + str(self.y) + self.symbol)



def parse_grid_file(graph, file_path):
    """
    ParseGridFile parses the grid file implementation from the file path line
    by line and construct the nodes & edges to be added to graph

    Returns graph object
    """
    # TODO: read the filepaht line by line to construct nodes & edges

    fil = open(file_path)

    rows =[]
    for line in fil:
        if line[0] == 'x':
            continue
        non_borders = line[1:-2]
        rows.append([non_borders[i:i+2] for i in range(0, len(non_borders), 2)])

        # fil.close()
    nodes = []
    edges = []

    y = 0
    for row in rows:
        x = 0
    
    for block in row:
        if block == '##':
            x += 1
            continue
            here_node = g.Node(Tile(x, y, block))
            nodes.append(here_node)

            adjacents = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
            for adjacent in adjacents:
                if adjacent[0] >= len(rows[0]) or adjacent[0] < 0 or adjacent[1] >= len(rows) or adjacent[1] < 0:
                    continue
                    dest_block = rows[adjacent[1]][adjacent[0]]
                    if dest_block == '##':
                     continue
                     to_node = g.Node(Tile(adjacent[0], adjacent[1], dest_block))
                     edges.append(g.Edge(here_node, to_node, 1))
            x += 1
        y += 1
 
    for node in nodes:
        status = graph.add_node(node)
        if not status:
            print('Failed to add grid node ' + str(node))
    for edge in edges:
        status = graph.add_edge(edge)
        if not status:
            print('Failed to add grid edge  ' + str(edge))
 
    
  # TODO: for each node/edge above, add it to graph

    return graph

def convert_edge_to_grid_actions(edges):
    """
    Convert a list of edges to a string of actions in the grid base tile

    e.g. Edge(Node(Tile(1, 2), Tile(2, 2), 1)) => "S"
    """
    if not edges:
        return ""
    
    actions = []
    for edge in edges:
        if edge.from_node.data.x > edge.to_node.data.x:
            actions.append('W')
        elif edge.from_node.data.x < edge.to_node.data.x:
            actions.append('E')
        elif edge.from_node.data.y > edge.to_node.data.y:
            actions.append('N')
        else:
            actions.append('S')
    
    return ''.join(actions)