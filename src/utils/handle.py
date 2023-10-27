from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.astar import astar
from algorithms.gbfs import gbfs
from algorithms.ucs import ucs
import output

algorithm_dict = {
    "bfs": bfs,
    "dfs": dfs,
    "astar": astar,
    "gbfs": gbfs,
    "ucs": ucs,
}

def handle(graph, algorithm, save_file_path):
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
    
    
    
    

        
