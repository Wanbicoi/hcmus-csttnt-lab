# hcmus-csttnt-lab

gắn link latex zô làm report nè, tui k biết làm :'<

Report: [Latex](https://github.com/Wanbicoi/hcmus-csttnt-lab/blob/main/README.md)

## Run program

clone this repo then execute

```
sh ./run.sh
```

**Required:** python >= 3.10

## Guildline :>

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
  x -> int
  y -> int

class Map:
  value -> Point[][]
  def input():
  def output():
```

The main.py will do following steps:
get input -> array of Graph

1. Get input -> [[Map, Map, ...], [Map, Map, ...], ...] -> [[Graph, Graph, ...], [Graph, Graph, ...], ...]
   DAT

2. Implement algorithms: each function takes input: Graph, output: Point[]
   TAN

   output -> route, traversed_nodes

3. Output:
   - Convert each Point[] to Map.
   - Write file: map-file.txt + jpg/mp4
     TRUNG

## References:

- [Video](https://www.facebook.com/nguyenthebinh288/videos/847813779289607)
- [Web](https://ngottrong.github.io/FindShortestPath/)
