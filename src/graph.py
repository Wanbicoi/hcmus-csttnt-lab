class Graph:
    def __init__(self):
        self.graph = {}

    # có gì đó sai sai, chưa xử lý trường hợp nếu point là điểm thưởng
    def add_edge(self, pointA, pointB, weight):
        if pointA in self.graph:
            self.graph[str(pointA)].append((pointB, weight))
            self.graph[str(pointB)].append((pointA, weight))
        else:
            self.graph[str( pointA )] = [pointA, weight]
            self.graph[str(pointB)] = [pointB, weight]
