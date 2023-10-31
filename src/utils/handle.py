from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.astar import astar1
from algorithms.astar import astar2
from algorithms.gbfs import gbfs1
from algorithms.gbfs import gbfs2
from algorithms.ucs import ucs
from algorithms.algo1 import algo1
from algorithms.algo1 import algo_1
from algorithms.algo2 import algo2
import output
import os
import time

algorithm_dict = {
    "bfs": bfs,
    "dfs": dfs,
    "ucs": ucs,
    "astar_heuristic_1": astar1,
    "astar_heuristic_2": astar2,
    "gbfs_heuristic_1": gbfs1,
    "gbfs_heuristic_2": gbfs2,
}

levels = ["level_1", "level_2", "level_3", "advance"]


def handle_level1(graphs, output_dir):
    inputs = ["input" + str(i) for i in range(1, len(graphs) + 1)]

    for i in range(len(graphs)):
        os.makedirs(output_dir + inputs[i], exist_ok=True)
        for algorithm in algorithm_dict:
            
            algo_dir = output_dir + inputs[i] + "/" + algorithm
            os.makedirs(algo_dir, exist_ok=True)
            start_time = time.time()
            traversed_nodes, route = algorithm_dict[algorithm](graphs[i])
            end_time = time.time()
            output.output(graphs[i], [], route, traversed_nodes, algo_dir)


def handle_level2(graphs, output_dir):
    inputs = ["input" + str(i) for i in range(1, len(graphs) + 1)]
    for i in range(len(graphs)):
        os.makedirs(output_dir + inputs[i], exist_ok=True)
        algo_dir = output_dir + inputs[i] + "/" + "algo_1"
        os.makedirs(algo_dir, exist_ok=True)
        traversed_nodelist, route = algo_1(graphs[i], graphs[i].heuristics2)
        output.output(
            graphs[i], graphs[i].bonus_nodes, route, traversed_nodelist, algo_dir
        )


def handle_level3(graphs, output_dir):
    inputs = ["input" + str(i) for i in range(1, len(graphs) + 1)]
    for i in range(len(graphs)):
        os.makedirs(output_dir + inputs[i], exist_ok=True)
        algo_dir = output_dir + inputs[i] + "/" + "algo2"
        os.makedirs(algo_dir, exist_ok=True)
        traversed_nodelist, route = algo2(graphs[i], graphs[i].heuristics2)
        output.output(
            graphs[i], graphs[i].pickup_nodes, route, traversed_nodelist, algo_dir
        )


def handle(graphs, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    for level in levels:
        os.makedirs(output_dir + level, exist_ok=True)
    # handle_level1(graphs[0], output_dir + "level_1/")
    handle_level2(graphs[1], output_dir + "level_2/")
    #handle_level3(graphs[2], output_dir + "level_3/")
