# hcmus-csttnt-lab
gắn link latex zô làm report nè, tui k biết làm :'<

Report: [Latex](https://github.com/Wanbicoi/hcmus-csttnt-lab/blob/main/README.md)

## Yêu cầu cơ bản: 

## Phương hướng đề xuất:

```
class Graph: 
  def __init__(self):
    self.graph = {}

  def add_edge(self, start, end, weight):
    if start in self.graph:
      self.graph[start].append((end, weight))
    else:
      self.graph[start] = [(end, weight)]
```

```
class Point:
  type -> "WALL", "NONE", "REWARD", "REQUIRED", "UP", "DOWN", "LEFT", "RIGHT"
  value -> int // if type == "REWARD"

class Map:
  value -> Point[][]
  def input():
  def output():
```
The main.py will do following steps:

1. Get input -> [[Map, Map, ...], [Map, Map, ...], ...] -> [[Graph, Graph, ...], [Graph, Graph, ...], ...]

2. Implement algorithms: each function takes input: Graph, output: Map

3. Output -> map-file.text

