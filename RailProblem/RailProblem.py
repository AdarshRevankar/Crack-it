from collections import defaultdict
import sys


def get_cost(path):
    price = 0
    for i in range(len(path) - 1):
        price += rail_cost[(path[i], path[i + 1])]
    return price


class Train:
    def __init__(self, path, cost):
        self.path = path
        self.cost = cost

    def __lt__(self, other):
        if self.cost < other.cost:
            return True
        elif self.cost == other.cost:
            if len(self.path) < len(other.path):
                return True
            elif len(self.path) == len(other.path):
                return str(self) < str(other)
        return False

    def __eq__(self, other):
        return self.cost == other.cost and str(self) == str(other)

    def __str__(self):
        return ' '.join(self.path) + ' ' + str(self.cost)


trains = []


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def get_path(self, u, d, visited, path):

        visited[u] = True
        path.append(u)
        if u == d:
            p = [index_to_place[x] for x in path]
            trains.append(Train(p, get_cost(p)))
        else:
            for i in self.graph[u]:
                if not visited[i]:
                    self.get_path(i, d, visited, path)
        path.pop()
        visited[u] = False

    def get_path_list(self, start, end):
        visited = [False] * self.V
        path = []
        self.get_path(start, end, visited, path)


# Get input
lines = sys.stdin.readlines()

source_stop, destination_stop = lines[0].split()
rail_cost = dict()
verts = set(source_stop)
verts.add(destination_stop)

for i in range(1, len(lines)):
    source, destination, cost = lines[i].split()
    # if destination in [x[1] for x in rail_cost.keys()]:
    #     for key, prev_val in rail_cost.items():
    #         rail_cost[(key[0], key[1]+"_")] = prev_val
    rail_cost[(source, destination)] = int(cost)
    verts.add(source)
    verts.add(destination)
place_to_index = {}
index_to_place = {}

for i, xi in zip(range(len(verts)), verts):
    place_to_index[xi] = i
    index_to_place[i] = xi

# Create a graph
g = Graph(len(verts))
for s, d in rail_cost.keys():
    g.add_edge(place_to_index[s], place_to_index[d])

g.get_path_list(place_to_index[source_stop],
                place_to_index[destination_stop])

if len(trains) == 0:
    print('No Trains')
else:
    trains.sort()
    for route in trains:
        print(route)
