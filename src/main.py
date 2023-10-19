from map import Map

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
