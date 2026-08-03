'''
Problem
Figure 1. The graph from the dataset

The task is to use breadth-first search to compute single-source shortest distances in an unweighted directed graph.

Given: A simple directed graph with n≤103 vertices in the edge list format.

Return: An array D[1..n] where D[i] is the length of a shortest path from the vertex 1 to the vertex i (D[1]=0). If i is not reachable from 1 set D[i] to −1.

See Figure 1 for visual example from the sample dataset.
Sample Dataset

6 6
4 6
6 5
4 3
3 5
2 1
1 4

Sample Output

0 -1 2 1 3 2
'''

from collections import deque

FILEPATH = r"BFS_breadth-first_search\data.txt"

def main():
    with open(FILEPATH) as file:
        lines = file.read().strip().splitlines()

    x, _ = map(int, lines[0].split())

    graph = {i: [] for i in range(1, x + 1)}
    for l in lines:
        a, b = map(int, l.split())
        graph[a].append(b)
    
    distance, visited = [-1] * (x + 1), [False] * (x + 1)
    distance[1], visited[1] = 0, True

    queue = deque([1])

    while queue:
        u = queue.popleft()
        for v in graph[v]:
            if not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + 1
                queue.append(v)

    print(' '.join(str(d) for d in distance[1:]))
    

if __name__ == "__main__":
    main()