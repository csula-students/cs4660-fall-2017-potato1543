"""
quiz2!
Use path finding algorithm to find your way through dark dungeon!
Tecchnical detail wise, you will need to find path from node 7f3dc077574c013d98b2de8f735058b4
to f1f131f647621a4be7c71292e79613f9
TODO: implement BFS """
"""
TODO: implement Dijkstra utilizing the path with highest effect number
"""

def bfs(graph,initial_id,dest_id):
     visited = {}
     parents = {}
     edges = {}
 
     q = []
     q.append((0, initial_id))
 
     visited[initial_id] = 0
     while len(q) != 0:
        a = get_state(q.pop()[1])
        neighbors = a['neighbors']
 
        for i in range(len(neighbors)):
            b = neighbors[i]
            if b['id'] not in visited:
                edge = transition_state(a['id'], b['id'])
                edges[b['id']] = edge
                visited[b['id']] = visited[a['id']] + 1
                parents[b['id']] = a['id']
 
              
                if b['id'] != dest_id:
                    q.append((visited[b['id']], b['id']))

        q.reverse()
       
        results = []
        node_id = dest_id

        if node_id in parents:
            results.append(edges[node_id])
            node_id = parents[node_id]
            
            results.reverse()
            
            return results


def Dikjstra(graph,initial_id,dest_id):
    visited = {}
    previous = {}
    edges = {}
 
    visited[initial_id] = 0
 
    q = []
    q.append((0, initial_id))
    visited = []
    if len(q) > 0:
        u = get_state(q.pop()[1])
        visited.append(u['id'])
        neighbors = u['neighbors']
     
    results = []
    node_id = dest_id
 
    if node_id in previous:
        results.append(edges[node_id])
        node_id = previous[node_id]
 
    results.reverse()
 
    return results

def print_path(graph,results,initial_id):
    prev_id = initial_id
    total = 0
    for i in range(len(results)):
        prev_node = get_state(prev_id)
        next_id = results[i]['id']
        total += results[i]['event']['effect']
        print("%s(%s):%s(%s):%i" % (prev_node['location']['name'], prev_id, results[i]['action'], results[i]['id'], results[i]['event']['effect']))
        prev_id = next_id
    print("\nTotal HP: %i" % total)

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
    initial_id = '7f3dc077574c013d98b2de8f735058b4'
    dest_id = 'f1f131f647621a4be7c71292e79613f9'
    empty_room = get_state('7f3dc077574c013d98b2de8f735058b4')
    print(empty_room)
    print(transition_state(empty_room['id'], empty_room['neighbors'][0]['id']))
    
    #Testing the BFS 
    results = bfs(graph,initial_id,dest_id)
    print("\n")
    print("BFS:")
    print_path(graph,results,initial_id)

    #Testing Dikjstra
    results = Dikjstra(graph,initial_id,dest_id)
    print("\n")
    print("Dikjstra:")
    print_path(graph,results,initial_id)