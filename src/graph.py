from collections import defaultdict
class Graph:
    '''
        Graph representation: adjacency list
        a node in graph: (i, j)
        -> graph[(i,j)] = [(i*, j*) ... adjacent to (i, j)]
        cost function: g
        heuristic function: h
        Each search algorithm in this graph returns
            ordered traversed nodes (for illustration)
            traversed path (if found) 
    '''
    def __init__(self, matrix, start, end, bonus_points=[], pickup_points=[]):
        self.graph = defaultdict(list)
        self.start = start
        self.end = end
        self.bonus_nodes = [(x[0], x[1]) for x in bonus_points]
        self.bonus_points = [x[2] for x in bonus_points]
        self.pickup_nodes = [(x[0], x[1]) for x in pickup_points]
        # initialize graph from given matrix
        self.graph[start] = self.get_adj_nodes(matrix, start[0], start[1])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(matrix[i][j] == " "):
                    self.graph[(i, j)] = self.get_adj_nodes(matrix, i, j)

    def valid_node(self, matrix, i, j):
        if(i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0])):
            return 0
        if(matrix[i][j] == " " or matrix[i][j] == "S"):
            return 1
        return 0
    
    def get_adj_nodes(self, matrix, row, col):
        next_row = [0, 1, -1, 0]
        next_col = [-1, 0, 0, 1]
        ls = []
        for i, j in zip(next_row, next_col):
            if(self.valid_node(matrix, row + i, col + j)):
                ls.append((row + i, col + j))
        return ls

    '''

    # có gì đó sai sai, chưa xử lý trường hợp nếu point là điểm thưởng
    def add_edge(self, pointA, pointB, weight):
        if pointA in self.graph:
            self.graph[str(pointA)].append((pointB, weight))
            self.graph[str(pointB)].append((pointA, weight))
        else:
            self.graph[str( pointA )] = [pointA, weight]
            self.graph[str(pointB)] = [pointB, weight]
    '''

