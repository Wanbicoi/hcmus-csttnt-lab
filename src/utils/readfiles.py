from graph import Graph
import os

input_path = "src/input"

def read_matrix(file_name: str):
    with open(file_name, 'r') as file:
        n_points = int(file.readline())
        points = []
        for _ in range(n_points):
            x, y, reward = map(int, file.readline().split(' '))
            points.append((x, y, reward))

        text = file.read()
        matrix = [list(i) for i in text.splitlines()]
            
        for i in range(len(matrix)):
          for j in range(len(matrix[0])):
            if matrix[i][j]=='S':
                start=(i,j)

            elif matrix[i][j]==' ':
                if (i==0) or (i==len(matrix)-1) or (j==0) or (j==len(matrix[0])-1):
                    end=(i,j)
                    
    return matrix, points, start, end

    
def read_files():
    input_paths = os.listdir(input_path)
    graph = []
    for path in input_paths:
      if (path == "level_1"):
          graph_level_1 = []
          input_level1 = [os.path.join(input_path, path, file) for file in os.listdir(os.path.join(input_path, path))]
          for file in input_level1:
            matrix, points, start, end = read_matrix(file)
            graph_level_1.append(Graph(matrix, start, end))
            
          graph.append(graph_level_1)
            
      elif (path == "level_2"):
          graph_level_2 = []
          input_level2 = [os.path.join(input_path, path, file) for file in os.listdir(os.path.join(input_path, path))]
          for file in input_level2:
            matrix, points, start, end = read_matrix(file)
            graph_level_2.append(Graph(matrix, start, end, points))
          graph.append(graph_level_2)
      
      elif (path == "level_3"):
          graph_level_3 = []
          input_level3 = [os.path.join(input_path, path, file) for file in os.listdir(os.path.join(input_path, path))]
          for file in input_level3:
            matrix, points, start, end = read_matrix(file)
            graph_level_3.append(Graph(matrix, start, end, [], points))
          graph.append(graph_level_3)
      elif (path == "advance"):
          graph_advance = []
          '''
          input_advance = [os.path.join(input_path, path, file) for file in os.listdir(os.path.join(input_path, path))]
          for file in input_advance:
            points, matrix, start, end = read_matrix(file)
            graph_advance.append(Graph(matrix, start, end, points))
          graph.append(graph_advance)
          '''        
      else:
        print("Invalid input path")
    return graph
   