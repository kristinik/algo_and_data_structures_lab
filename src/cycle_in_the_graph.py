from collections import deque

def has_cycle(graph):
    visited = set()
    for start_node in graph:
        if start_node not in visited:
            queue = deque()
            start_node_with_parent = (start_node, None)
            queue.append(start_node_with_parent)
            while queue:
                current_node, parent = queue.popleft()
                visited.add(current_node)
                for neighbor in graph[current_node]:
                    if neighbor != parent:
                        if neighbor in visited:
                            return True
                        queue.append((neighbor, current_node))
    return False

def read_graph_from_file(file_name):
    graph = {}
    with open(file_name, 'r') as file:
        for line in file:
            nodes = line.strip().split()
            node = int(nodes[0])
            neighbors = [int(x) for x in nodes[1:]]
            graph[node] = neighbors
    return graph

def write_result_to_file(result, file_name):
    with open(file_name, 'w') as file:
        file.write(str(result))

if __name__ == "__main__":
    graph = read_graph_from_file("resources/input.txt")
    result = has_cycle(graph)
    write_result_to_file(result, "resources/output.txt")