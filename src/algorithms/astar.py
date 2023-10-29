from collections import defaultdict
from queue import PriorityQueue as pq

def astar(graph, heuristics):
    open = pq()
    open.put((heuristics(graph.start, graph.end), 0, graph.start, graph.start)) 
    close = defaultdict(int) 
    traversed_nodes = []
    prev = defaultdict(tuple) 
    route = [] 
    while not open.empty():
        f, g, cur_node, prev_node = open.get()
        if cur_node == graph.end:
            prev[cur_node] = prev_node
            traversed_nodes.append(cur_node)
            break
        if close[cur_node] != 1:
            close[cur_node] = 1
            prev[cur_node] = prev_node
            traversed_nodes.append(cur_node)
            for node in graph.graph[cur_node]:
                if not close[node]:
                    open.put((g + graph.cost + heuristics(node, graph.end), g + graph.cost, node, cur_node))
                    
    if prev[graph.end] == tuple():
        return traversed_nodes, route
    else:
        node = graph.end
        while prev[node] != graph.start:
            route.append(node)
            node = prev[node]
        route.append(node)
        route.append(graph.start)
        route.reverse()
        return traversed_nodes, route
        