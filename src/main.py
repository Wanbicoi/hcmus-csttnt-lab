from utils.readfiles import read_files
from utils.createmap import create_map
from graph import Graph
from algorithms.bfs import bfs
from algorithms.dfs import dfs
import output
from utils.handle import handle
import os



if __name__ == "__main__":
   graphs = read_files() # [[Graph x 5], [Graph x 3], [Graph x 3]]
   output_path = ["src/output/level_1"] # "src/output/level_2", "src/output/level_3", "src/output/advance"
   algorithms = ["gbfs", "astar"] # "bfs", "dfs", "ucs", 
   for i in range(len(graphs)):
       for j in range(len(graphs[i])):
           for k in range(len(algorithms)):
               handle(graphs[i][j], algorithms[k], os.path.join(output_path[i], algorithms[k]))
               
   
   
      
   
   
   