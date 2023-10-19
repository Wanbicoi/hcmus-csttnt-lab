class Point:
    def __init__(self, x:int, y:int, weight:int, type: str) -> None:
        self.x = x
        self.y = y
        self.type = (
            type  # "WALL", "NONE", "REWARD", "REQUIRED", "UP", "DOWN", "LEFT", "RIGHT"
        )
        self.weight = weight
        self.visited = False

    def __str__(self) -> str:
        return f"({self.x} {self.y})"


