from collections import defaultdict
from queue import PriorityQueue as pq

def algo1(graph, heuristics):
    bonus_list = [(heuristics(bonus_node, graph.end), bonus_point, bonus_node) for bonus_node, bonus_point in zip(graph.bonus_nodes, graph.bonus_points)]
    bonus_list.sort()
    # set goal list from bonus list
    goal_list = [graph.end]
    for h, point, node in bonus_list:
        goal = goal_list[-1]
        if h + point + heuristics(graph.start, node) < heuristics(graph.start, goal):
            goal_list.append(node)
 
    traversed_nodelist = []
    prev = defaultdict(tuple) 
    route = []
    start = graph.start
    prev[start] = start
    # search for each sub-route
    while len(goal_list) > 0:
        traversed_nodes = []
        goal = goal_list[-1]
        open = pq() 
        open.put((heuristics(start, goal), 0, start, prev[start]))
        # set temporary close for sub-route
        close = defaultdict(int)
        while not open.empty():
            f, g, cur_node, prev_node = open.get()
            if cur_node == goal:
                prev[cur_node] = prev_node
                traversed_nodes.append(cur_node)
                break
                
            if not close[cur_node]:
                close[cur_node] = 1
                prev[cur_node] = prev_node
                traversed_nodes.append(cur_node)
                for node in graph.graph[cur_node]:
                    if not close[node]:
                        open.put((g + graph.cost + heuristics(node, goal), g + graph.cost, node, cur_node))
        goal_list.pop()
        traversed_nodelist.append(traversed_nodes)
        if prev[goal] != tuple():
            # if found the goal, update the starting node, route, and close the node on route
            node = goal
            temp_route = []
            while node != start:
                temp_route.append(node)
                node = prev[node]
            temp_route.append(start)
            temp_route.reverse()
            route.extend(temp_route)
            start = goal 
    for traversed in traversed_nodelist:
        print(traversed)
    return traversed_nodelist, route