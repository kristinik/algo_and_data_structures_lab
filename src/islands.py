import csv

class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root_vertex1 = self.find(vertex1)
        root_vertex2 = self.find(vertex2)

        if root_vertex1 == root_vertex2:
            return False

        if self.rank[root_vertex1] < self.rank[root_vertex2]:
            self.parent[root_vertex1] = root_vertex2
        elif self.rank[root_vertex1] > self.rank[root_vertex2]:
            self.parent[root_vertex2] = root_vertex1
        else:
            self.parent[root_vertex2] = root_vertex1
            self.rank[root_vertex1] += 1

        return True

def kruskal_mst(graph):
    vertex_count = len(graph)
    edges = []
    for i in range(vertex_count):
        for j in range(i + 1, vertex_count):
            if graph[i][j] != 0:
                edges.append((graph[i][j], i, j))

    edges.sort()
    mst = []
    ds = DisjointSet(vertex_count)

    for edge in edges:
        weight, vertex1, vertex2 = edge
        if ds.union(vertex1, vertex2):
            mst.append(edge)

    total_weight = sum(edge[0] for edge in mst)
    return total_weight

import os

def read_graph(file_name):
    graph = {}

    file_path = os.path.abspath(file_name)

    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        adjacency_matrix = [list(map(int, row)) for row in csv_reader]

        num_islands = len(adjacency_matrix)

        for i in range(num_islands):
            for j in range(num_islands):
                if adjacency_matrix[i][j] != 0:
                    if str(i) not in graph:
                        graph[str(i)] = {}
                    graph[str(i)][str(j)] = adjacency_matrix[i][j]

    return "0", str(num_islands - 1), graph
