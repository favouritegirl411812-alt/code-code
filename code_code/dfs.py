
def dfs(graph, start):
    visited = set()
    stack = [start]
    traversal = []

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            traversal.append(node)

            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return traversal


def run_dfs():
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }

    print("DEPTH FIRST SEARCH")
    result = dfs(graph, 'A')
    print("DFS Traversal:", result)

    return result


if __name__ == "__main__":
    run_dfs()
