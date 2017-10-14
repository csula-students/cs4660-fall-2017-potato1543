"""
quiz2!
Use path finding algorithm to find your way through dark dungeon!
Tecchnical detail wise, you will need to find path from node 7f3dc077574c013d98b2de8f735058b4
to f1f131f647621a4be7c71292e79613f9
TODO: implement BFS """

def bfs(graph,initial_node):
    dest_node = f1f131f647621a4be7c71292e79613f9
    #keeps track of the visited nodes
    visited = []
    #keep track of nodes to be checked
    queue = [initial_node]

    #keep looping until there are nodes still to be checked
    while queue:
        #pop first node from queue
        node = queue.pop(0)
        if node not in dest_node:
            return True
        
        for i in self.graph[node]:
            if visited[i] == False:
                queue.append(i)
                neighbors = self.graph[node]
                visited[i] = True
    # If BFS completes without getting to dest_node
    return False

"""
TODO: implement Dijkstra utilizing the path with highest effect number
"""

import json
import codecs
import graph

# http lib import for Python 2 and 3: alternative 4
try:
    from urllib.request import urlopen, Request
except ImportError:
    from urllib2 import urlopen, Request

GET_STATE_URL = "http://192.241.218.106:9000/getState"
STATE_TRANSITION_URL = "http://192.241.218.106:9000/state"

def get_state(room_id):
    """
    get the room by its id and its neighbor
    """
    body = {'id': room_id}
    return __json_request(GET_STATE_URL, body)

def transition_state(room_id, next_room_id):
    """
    transition from one room to another to see event detail from one room to
    the other.
    You will be able to get the weight of edge between two rooms using this method
    """
    body = {'id': room_id, 'action': next_room_id}
    return __json_request(STATE_TRANSITION_URL, body)

def __json_request(target_url, body):
    """
    private helper method to send JSON request and parse response JSON
    """
    req = Request(target_url)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    jsondata = json.dumps(body)
    jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
    req.add_header('Content-Length', len(jsondataasbytes))
    response = json.load(urlopen(req, jsondataasbytes))
    return response

if __name__ == "__main__":
    # Your code starts here
     g = self.graph
    empty_room = get_state('7f3dc077574c013d98b2de8f735058b4')
    g.bfs(g,empty_room)
    print(empty_room)
    print(transition_state(empty_room['id'], empty_room['neighbors'][0]['id']))
