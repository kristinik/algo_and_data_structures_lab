
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        return True


def kruskal_mst(graph):
    n = len(graph)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if graph[i][j] != 0:
                edges.append((graph[i][j], i, j))

    edges.sort()
    mst = []
    ds = DisjointSet(n)

    for edge in edges:
        weight, u, v = edge
        if ds.union(u, v):
            mst.append(edge)

    total_weight = sum(weight for weight, _, _ in mst)
    return total_weight

def read_graph(file_path):
    graph = {}

    with open(file_path, 'r') as file:
        adjacency_matrix = [list(map(int, line.strip().split(','))) for line in file]

        num_islands = len(adjacency_matrix)

        for i in range(num_islands):
            for j in range(num_islands):
                if adjacency_matrix[i][j] != 0:
                    if str(i) not in graph:
                        graph[str(i)] = {}
                    graph[str(i)][str(j)] = adjacency_matrix[i][j]

    return "0", str(num_islands - 1), graph

start, finish, graph_data = read_graph('../resources/islands.csv')

