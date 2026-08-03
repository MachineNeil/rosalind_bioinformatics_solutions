'''
Problem
Figure 1. The graph from the dataset

The task is to use depth-first search to compute the number of connected components in a given undirected graph.

Given: A simple graph with n≤103 vertices in the edge list format.

Return: The number of connected components in the graph.

See Figure 1 for visual example from the sample dataset.
Sample Dataset

12 13
1 2
1 5
5 9
5 10
9 10
3 4
3 7
3 8
4 8
7 11
8 11
11 12
8 12

Sample Output

3
'''

FILEPATH = r"CC_connected_components\data.txt"

def depth_first_search(array, adjacency_list, visited):
    stack = [array]
    visited[array] = False

    while stack:
        node = stack.pop()
        for neighbor in adjacency_list[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                stack.append(neighbor)

def main():
    with open(FILEPATH) as file:
        lines = file.read().strip().splitlines()

    n, m = map(int, lines[0].split())
    adjacency_list = {i: [] for i in range(1, n + 1)}

    for l in lines[1:(m + 1)]:
        a, b = map(int, l.split())
        adjacency_list[a].append(b)
        adjacency_list[b].append(a)

    visited = [True] * (n + 1)
    components = 0
    for v in range(1, n + 1):
        if not visited[v]:
            components += 1
            depth_first_search(v, adjacency_list, visited)

    print(components)

if __name__ == "__main__":
    main()