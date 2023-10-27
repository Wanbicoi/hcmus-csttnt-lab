from queue import PriorityQueue as pq
from collections import defaultdict 
def ucs(g):
    open = pq()
    open.put((0, g.start))
    close = defaultdict(int)
    traversed_nodes = []
    prev = defaultdict(list) 
    route = []
    
    while not open.empty():
        dist, cur_node = open.get()
        close[cur_node] = 1
        traversed_nodes.append(cur_node)
        if cur_node == g.end:
            break
        for node in g.graph[cur_node]:
            if not close[node]:
                open.put((dist + g.cost, node))
                prev[node] = cur_node
    if prev[g.end] == tuple():
        return traversed_nodes, route
    else:
        node = g.end
        while prev[node] != g.start:
            route.append(node)
            node = prev[node]
        route.append(node)
        route.append(g.start)
        route.reverse()
        return traversed_nodes, route
        