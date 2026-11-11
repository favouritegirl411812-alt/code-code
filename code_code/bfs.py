
from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    traversal = []

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            traversal.append(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return traversal


def run_bfs():
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    print("BREADTH FIRST SEARCH")
    result = bfs(graph, 'A')
    print("BFS Traversal:", result)

    return result


if __name__ == "__main__":
    run_bfs()
