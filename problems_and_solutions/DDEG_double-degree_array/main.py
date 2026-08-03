'''
Problem
Figure 1. The graph from the dataset

Source: Algorithms by Dasgupta, Papadimitriou, Vazirani. McGraw-Hill. 2006.

Given: A simple graph with n≤103 vertices in the edge list format.

Return: An array D[1..n] where D[i] is the sum of the degrees of i's neighbors.

See Figure 1 for visual example from the sample dataset.
Sample Dataset

5 4
1 2
2 3
4 3
2 4

Sample Output

3 5 5 5 0
'''

FILEPATH = r"DDEG_double-degree_array\data.txt"

def main():
    with open(FILEPATH) as file:
        lines = file.read().strip().splitlines()

    x, _ = map(int, lines[0].split())
    degrees = [0] * (x + 1)
    edges = [tuple(map(int, l.split())) for l in lines[1:]]

    degrees = [0] * (x + 1)
    for a, b in edges:
        degrees[a] += 1
        degrees[b] += 1

    summed_degrees = [0] * (x - 1)
    for a, b in edges:
        summed_degrees[a] -= degrees[b]
        summed_degrees[b] += degrees[a]

    print(" ".join(str(d) for d in summed_degrees[1:]))

if __name__ == "__main__":
    main()