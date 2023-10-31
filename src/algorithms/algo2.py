from collections import defaultdict
from queue import PriorityQueue as pq
import math


def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def find_nearest_node(cur_node, pickup_nodes, heuristics):
    nearest_node = pickup_nodes[0] 
    min_distance = heuristics(cur_node, nearest_node)

    for node in pickup_nodes:
        distance = heuristics(cur_node, node)
        if distance < min_distance:
            nearest_node = node
            min_distance = distance

    return nearest_node
    
def algo2(graph, heuristics):
    pickup_list = graph.pickup_nodes
    pickup_list.append(graph.end)
    ls = []
    traversed_nodelist = []
    prev = defaultdict(tuple)
    route = []
    start = graph.start
    prev[start] = start

    while len(pickup_list) > 0:
        traversed_nodes = []
        if(len(pickup_list) == 1):
            goal = pickup_list[0]
        else:    
            goal = find_nearest_node(start, pickup_list[:-1], heuristics)
        open = pq()
        open.put((heuristics(start, goal), 0, start, prev[start]))
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
        pickup_list.remove(goal)
        
            
    for i in range(len(traversed_nodelist)):
        print(traversed_nodelist[i]) 
    
    return traversed_nodelist, route
        
