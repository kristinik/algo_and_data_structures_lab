from collections import defaultdict

def dfs(node, graph, visited, result):
    visited.add(node)
    if node in graph:
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, graph, visited, result)
    result.append(node)

def topological_sort(graph):
    visited = set()
    result = []
    keys = list(graph.keys())
    for node in keys:
        if node not in visited:
            dfs(node, graph, visited, result)
    return result[::-1]

def read_input(filename):
    graph = defaultdict(list)
    with open(filename, 'r') as f:
        for line in f:
            dependency, dependent = line.strip().split()
            graph[dependent].append(dependency)
    return graph

def write_output(filename, order):
    with open(filename, 'w') as f:
        for node in order:
            f.write(node + '\n')

def main():
    graph = read_input('../resources/govern.in')
    sorted_nodes = topological_sort(graph)
    write_output('../resources/govern.out', sorted_nodes)

if __name__ == "__main__":
    main()


