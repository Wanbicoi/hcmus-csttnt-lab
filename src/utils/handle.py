from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.astar import astar
from algorithms.gbfs import gbfs
from algorithms.ucs import ucs
import output
import os

algorithm_dict = {
    "bfs": bfs,
    "dfs": dfs,
    "astar": astar,
    "gbfs": gbfs,
    "ucs": ucs,
}

def handle(graph, algorithm, save_file_path):
    if (algorithm == "bfs" or algorithm == "dfs" or algorithm == "ucs"):
        traversed_nodes, route = algorithm_dict[algorithm](graph)
        output.output(
            graph.matrix,
            graph.bonus_points,
            graph.start,
            graph.end,
            route,
            traversed_nodes,
            save_file_path,
        )
    else:
        traversed_nodes, route = algorithm_dict[algorithm](graph, graph.heuristics)
        output.output(
            graph.matrix,
            graph.bonus_points,
            graph.start,
            graph.end,
            route,
            traversed_nodes,
            save_file_path + "1",
        )
        traversed_nodes, route = algorithm_dict[algorithm](graph, graph.heuristics2)
        output.output(
            graph.matrix,
            graph.bonus_points,
            graph.start,
            graph.end,
            route,
            traversed_nodes,
            save_file_path + "2",
        )
    
    
    

        
