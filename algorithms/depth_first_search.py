def dfs(graph, start_node):

    visit = list()
    stack = list()

    stack.append(start_node)

    while stack:
        
        node = stack.pop()
        
        if node not in visit:
            visit.append(node)
            print(graph[node])
            stack.extend(graph[node])


if __name__ == "__main__":
    graph = {
        'A': ['B'],
        'B': ['A', 'C', 'H'],
        'C': ['B', 'D', 'G'],
        'D': ['C', 'E'],
        'E': ['D', 'F'],
        'F': ['E'],
        'G': ['D'],
        'H': ['B', 'I', 'J', 'M'],
        'I': ['H'],
        'J': ['H', 'K'],
        'K': ['J', 'L'],
        'L': ['K'],
        'M': ['H']
    }

    print(dfs(graph, 'A'))