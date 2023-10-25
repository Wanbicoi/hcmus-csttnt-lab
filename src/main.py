from utils.readfiles import read_file
from utils.createmap import create_map
from graph import Graph
from algorithms.bfs import bfs
from output import output

input_paths = [
    "src/input/level_1",
    "src/input/level_2",
    "src/input/level_3",
    "src/input/advance",
]

output_paths = [
    "src/output/level_1",
    "src/output/level_2",
    "src/output/level_3",
    "src/output/advance",
]


# refact to other file if you want 😃
end = (-1, -1)
start = (-1, -1)
create_map()
bonus_points, matrix = read_file("maze_map.txt")
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] == "S":
            start = (i, j)

        elif matrix[i][j] == " ":
            if (
                (i == 0)
                or (i == len(matrix) - 1)
                or (j == 0)
                or (j == len(matrix[0]) - 1)
            ):
                end = (i, j)

        else:
            pass
graph = Graph(matrix, start, end)
traversed_nodes, route = bfs(graph)

# NOTE: change output_path
output(matrix, bonus_points, start, end, route, traversed_nodes, output_paths[0])
