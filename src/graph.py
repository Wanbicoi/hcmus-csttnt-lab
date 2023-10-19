class Graph:
    def __init__(self):
        self.graph = {}

    # có gì đó sai sai, chưa xử lý trường hợp nếu point là điểm thưởng
    def add_edge(self, pointA, pointB, weight):
        if pointA in self.graph:
            self.graph[pointA].append((pointB, weight))
            self.graph[pointB].append((pointA, weight))
        else:
            self.graph[pointA] = [pointA, weight]
            self.graph[pointB] = [pointB, weight]
