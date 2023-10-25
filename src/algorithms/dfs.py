from collections import defaultdict
def dfs(g):
    print(g.start)
    print(g.end)
    open = [g.start] # stack, contain nodes to traverse next
    close = defaultdict(int) # check node traversed or not
    traversed_nodes = [] # list containing ordered traversed nodes
    prev = defaultdict(list) # contain the previous node to trace the route
    route = [] # route from start to end
    while len(open) > 0:
        cur_node = open.pop()
        close[cur_node] = 1
        traversed_nodes.append(cur_node)
        if cur_node == g.end:
            break
        for node in g.graph[cur_node]:
            if not close[node]:
                open.append(node)
                prev[node] = cur_node
    
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
        



