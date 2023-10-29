from collections import defaultdict
from queue import PriorityQueue as pq

def gbfs1(graph):
    return gbfs(graph, graph.heuristics)
def gbfs2(graph):
    return gbfs(graph, graph.heuristics2)

def gbfs(g, heuristics):
    open = pq()
    open.put((heuristics(g.start, g.end), g.start, g.start))
    close = defaultdict(int) 
    traversed_nodes = [] 
    prev = defaultdict(tuple) 
    route = [] 
    while not open.empty():
        h, cur_node, prev_node = open.get()
        if close[cur_node] == 1:
            continue
        close[cur_node] = 1
        traversed_nodes.append(cur_node)
        prev[cur_node] = prev_node
        if cur_node == g.end:
            break
        for node in g.graph[cur_node]:
            if not close[node]:
                open.put((heuristics(node, g.end), node, cur_node))
    
    if prev[g.end] == tuple():
        return traversed_nodes, route # route is empty
    else:
        node = g.end
        while prev[node] != g.start:
            route.append(node)
            node = prev[node]
        route.append(node)
        route.append(g.start)
        route.reverse()
        return traversed_nodes, route
        