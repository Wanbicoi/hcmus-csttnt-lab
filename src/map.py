from point import Point
from graph import Graph


class Map:
    def __init__(self) -> None:
        self.value: list[list[Point]] = []
        self.ITEM: dict = {"x": "WALL", "S": "WALL", "+": "REWARD", " ": "NONE"}

    def input(self, file_name: str):
        try:
            with open(file_name, "r") as file:
                content = file.read()
                # Split the content into lines
                lines = content.split("\n")

                n = int(lines[0])
                self.width = len(lines[n + 1])
                self.height = (len(lines) - 1) - (n + 1)
                for x in range(self.height):
                    row: list = []
                    for y in range(self.width):
                        row.append(Point(x, y, 0, self.ITEM[lines[x + n + 1][y]]))
                        # Find EXIT point
                        if (
                            # must on the edge
                            (x == 0 or x == self.height or y == 0 or y == self.width)
                            # must not on the corner
                            and (x != self.height - 1 and y != 0)
                            and (x != self.height - 1 and y != self.height - 1)
                            and (y != self.height - 1 and x != 0)
                            and (y != 0 and x != 0)
                            # must equal to " "
                            and lines[x + n + 1][y] == " "
                        ):
                            self.exit = Point(x, y, 0, "EXIT")

                        # Find Start point
                        if lines[x + n + 1][y] == "S":
                            self.start = Point(x, y, 0, "START")
                    self.value.append(row)

                # Update REWARD
                for i in range(n):
                    items = lines[i + 1].split(" ")
                    x = int(items[0])
                    y = int(items[1])
                    self.value[x][y].weight = -int(items[2])

        except FileNotFoundError:
            print(f"File not found: {file_name}")

    def toGraph(self) -> Graph:
        DIRECTIONS: list[list] = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        graph = Graph()
        queue: list[Point] = []
        queue.append(self.start)

        while len(queue):
            point = queue.pop(0)

            for direction in DIRECTIONS:
                nextX = point.x - direction[0]
                nextY = point.y - direction[1]
                if (
                    # make sure next Point inside Map
                    nextX >= 0
                    and nextX < self.height
                    and nextY >= 0
                    and nextY < self.width
                    # make sure next Point is not WALL
                    and self.value[nextX][nextY].type != "WALL"
                    # make sure next Point is not visited
                    and self.value[nextX][nextY].visited == False
                ):
                    self.value[nextX][nextY].visited = True
                    graph.add_edge(point, self.value[nextX][nextY], 0)
                    queue.append(self.value[nextX][nextY])

        return graph

    def __str__(self) -> str:
        res = ""
        for row in self.value:
            for element in row:
                res += str(element)
            res += "\n"
        return res
