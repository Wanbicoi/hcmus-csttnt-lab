from collections import defaultdict
from queue import PriorityQueue as pq
import math

def astar(graph, heuristics, start, end):
    open = pq()
    open.put((heuristics(start, end), 0, start, start))
    close = defaultdict(int)
    traversed_nodes = []
    prev = defaultdict(tuple)
    route = []

    while not open.empty():
        f, g, cur_node, prev_node = open.get()
        if cur_node == end:
            prev[cur_node] = prev_node
            traversed_nodes.append(cur_node)
            break
        if close[cur_node] != 1:
            close[cur_node] = 1
            prev[cur_node] = prev_node
            traversed_nodes.append(cur_node)
            for node in graph.graph[cur_node]:
                if not close[node]:
                    open.put((g + graph.cost + heuristics(node, end), g + graph.cost, node, cur_node))

    if prev[end] == tuple():
        return traversed_nodes, route
    else:
        node = end
        while node != start:
            route.append(node)
            node = prev[node]
        route.append(start)
        route.reverse()
        return traversed_nodes, route


def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


def find_nearest_node(current, pickup_nodes):
    nearest_node = pickup_nodes[0] 
    min_distance = manhattan_distance(current, nearest_node)

    for node in pickup_nodes:
        distance = manhattan_distance(current, node)
        if distance < min_distance:
            nearest_node = node
            min_distance = distance

    return nearest_node
    
def algo2(graph, heuristics):
    pickup_list = []
    pickup_list.append(graph.start)
    while graph.pickup_nodes:
        nearest_node = find_nearest_node(pickup_list[-1], graph.pickup_nodes)
        pickup_list.append(nearest_node)
        graph.pickup_nodes.remove(nearest_node)
    pickup_list.append(graph.end)
    
    print(pickup_list)
    
    traversed_nodes = []
    route = []
    for i in range(len(pickup_list) - 1):
        temp_traversed_nodes, temp_route = astar(graph, heuristics, pickup_list[i], pickup_list[i + 1])
        traversed_nodes += temp_traversed_nodes
        route += temp_route
    
    
    return traversed_nodes, route
    
    