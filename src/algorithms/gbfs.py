from collections import defaultdict
def gbfs(g, heuristics):
    open = (heuristics(g.start, g.end), g.start) # open only 1 node
    close = defaultdict(int) 
    traversed_nodes = [] 
    prev = defaultdict(list) 
    route = [] 
    while True:
        h, cur_node = open
        close[cur_node] = 1
        traversed_nodes.append(cur_node)
        if cur_node == g.end:
            break
        higher_node = cur_node
        max_height = h
        for node in g.graph[cur_node]:
            if not close[node]:
                if heuristics(node, g.end) < max_height:
                    higher_node = node
                    max_height = heuristics(node, g.end)
        if higher_node != cur_node:
            open = (max_height, higher_node)
            prev[higher_node] = cur_node
        else:
            break
    
    if prev[g.end] == []:
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
        