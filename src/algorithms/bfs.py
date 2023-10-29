from queue import Queue
from collections import defaultdict

def bfs(g):  # input
    open = Queue()
    open.put((g.start, g.start))  # queue, contain nodes to traverse next
    close = defaultdict(int)  # check node traversed or not

    traversed_nodes = []  # list containing ordered traversed nodes
    prev = defaultdict(tuple)  # contain the previous node to trace the route
    route = []  # route from start to end

    while not open.empty():
        cur_node, prev_node = open.get()
        if close[cur_node] == 1:
            continue
        close[cur_node] = 1
        traversed_nodes.append(cur_node)
        prev[cur_node] = prev_node
        if cur_node == g.end:
            break
        for node in g.graph[cur_node]:
            if not close[node]:
                open.put((node, cur_node))
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
