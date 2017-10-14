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
     distance = {}
     parents = {}
     edges = {}
 
     q = []
     q.append((0, initial_id))
 
     distance[initial_id] = 0
     while len(q) > 0:
        u = get_state(q.pop()[1])
        neighbors = u['neighbors']
 
        for i in range(len(neighbors)):
            v = neighbors[i]
            if v['id'] not in distance:
                edge = transition_state(u['id'], v['id'])
                edges[v['id']] = edge
                distance[v['id']] = distance[u['id']] + 1
                parents[v['id']] = u['id']
 
                # continue to enqueue if we haven't reached the end
                if v['id'] != dest_id:
                    q.append((distance[v['id']], v['id']))
 
         # sort priority
        q = sorted(q, key=lambda x:x[0])
        q.reverse()
        # actions is a list of edges
        actions = []
        node_id = dest_id

        if node_id in parents:
            actions.append(edges[node_id])
            node_id = parents[node_id]
            
            # reverse the list of edges
            actions.reverse()
            
            return actions


def Dikjstra(graph,initial_id,dest_id):
    distance = {}
    previous = {}
    edges = {}
 
    distance[initial_id] = 0
 
    q = []
    q.append((0, initial_id))
    visited = []
    while len(q) > 0:
        u = get_state(q.pop()[1])
        visited.append(u['id'])
        neighbors = u['neighbors']
 
        for i in range(len(neighbors)):
            v = neighbors[i]
            edge = transition_state(u['id'], v['id'])
            alt = distance[u['id']] + edge['event']['effect']
 
            if v['id'] not in visited and (v['id'] not in distance or alt > distance[v['id']]):
                # reassign priority
                if v['id'] in distance:
                    q.remove((distance[v['id']], v['id']))
                # enqueue v for further evaluations
                q.append((alt, v['id']))
 
                distance[v['id']] = alt
                previous[v['id']] = u['id']
                edges[v['id']] = edge
 
        # sort priority
        q = sorted(q, key=lambda x:x[0])
     
    actions = []
    node_id = dest_id
 
    while node_id in previous:
        actions.append(edges[node_id])
        node_id = previous[node_id]
 
    actions.reverse()
 
    return actions

def print_actions(actions,initial_id):
    prev_id = initial_id
    total = 0
    for i in range(len(actions)):
        prev_node = get_state(prev_id)
        next_id = actions[i]['id']
        total += actions[i]['event']['effect']
        print("%s(%s):%s(%s):%i" % (prev_node['location']['name'], prev_id, actions[i]['action'], actions[i]['id'], actions[i]['event']['effect']))
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
    actions = bfs(graph,initial_id,dest_id)
    print("\n")
    print("BFS:")
    print_actions(actions,initial_id)

    #Testing Dikjstra
    actions = Dikjstra(graph,initial_id,dest_id)
    print("\n")
    print("Dikjstra:")
    print_actions(actions,initial_id)