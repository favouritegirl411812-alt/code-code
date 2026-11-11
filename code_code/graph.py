
def dfs(graph, start):
    """Perform Depth First Search using a stack."""

    visited = set()
    stack = [start]
    traversal = []

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            traversal.append(node)

            # Add adjacent nodes to the stack
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return traversal


def run_dfs():
    """Experiment 10: Depth First Search."""

    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    print("DEPTH FIRST SEARCH")
    print("Graph:", graph)

    result = dfs(graph, 'A')

    print("DFS Traversal:", result)

    return result

from collections import deque


def bfs(graph, start):
    """Perform Breadth First Search using a queue."""

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
    """Experiment 11: Breadth First Search."""

    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    print("BREADTH FIRST SEARCH")
    print("Graph:", graph)

    result = bfs(graph, 'A')

    print("BFS Traversal:", result)

    return result
