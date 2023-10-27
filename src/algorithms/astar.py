from collections import defaultdict

def astar(g, heuristics):
    open = (g.cost + heuristics(g.start, g.end), g.start) # open only 1 node
    close = defaultdict(int) 
    traversed_nodes = [] 
    prev = defaultdict(list) 
    route = [] 
    while True:
        f, cur_node = open
        close[cur_node] = 1
        traversed_nodes.append(cur_node)
        if cur_node == g.end:
            break
        next_node = cur_node
        max = f
        candidates = []
        for node in g.graph[cur_node]:
            if not close[node]:
                if g.cost + heuristics(node, g.end) < max:
                    next_node = node
                    max = g.cost + heuristics(node, g.end)
                candidates.append((node, g.cost + heuristics(node, g.end)))
        if next_node != cur_node:
            open = (max, next_node)
            prev[next] = cur_node
        else:
            next_node2 = cur_node
            for candidate_f, candidate_node in candidates:
                for node in g.graph[candidate_node]:
                    if not close[node]:
                        if g.cost + heuristics(node, g.end) < max:
                            next_node = candidate_node
                            next_node2 = node
                            max = g.cost + heuristics(node, g.end)
            if next_node != cur_node:
                close(next_node)
                open = (max, next_node2)
                prev[next_node] = cur_node
                prev[next_node2] = next_node
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
        