from map import Map
from utils.readfiles import read_file
from utils.visualization import visualize_maze
from utils.createmap import create_map
from graph import Graph
from algorithms.bfs import bfs
from algorithms.dfs import dfs
'''
paths = [
    "src/input/level_1",
    "src/input/level_2",
    "src/input/level_3",
    "src/input/advance",
]

map = Map()
map.input("src/input/level_1/input2.txt")
graph = map.toGraph()

print(map)
'''

if __name__ == "__main__":
    create_map()
    bonus_points, matrix = read_file('maze_map.txt')
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]=='S':
                start=(i,j)

            elif matrix[i][j]==' ':
                if (i==0) or (i==len(matrix)-1) or (j==0) or (j==len(matrix[0])-1):
                    end=(i,j)

            else:
                pass
    graph = Graph(matrix, start, end)
    traversed_nodes, route = bfs(graph)
    visualize_maze(matrix,bonus_points,start,end,route)
    print(traversed_nodes)
    print(route)