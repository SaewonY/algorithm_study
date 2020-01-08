from queue import Queue

def bfs(graph, start_node):

    visit = set() 
    q = Queue()
    q.put(start_node)

    while q.qsize() > 0:
        
        node = q.get()

        if node not in visit: 
            visit.add(node)
            for nextNode in graph[node]:
                q.put(nextNode)

    return visit



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

    print(bfs(graph, 'A'))