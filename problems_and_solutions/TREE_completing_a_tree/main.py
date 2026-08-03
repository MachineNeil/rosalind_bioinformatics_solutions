'''
Problem
Figure 2. A labeled tree with 6 vertices and 5 edges.

An undirected graph is connected if there is a path connecting any two nodes. A tree is a connected (undirected) graph containing no cycles; this definition forces the tree to have a branching structure organized around a central core of nodes, just like its living counterpart. See Figure 2.

We have already grown familiar with trees in “Mendel's First Law”, where we introduced the probability tree diagram to visualize the outcomes of a random variable.

In the creation of a phylogeny, taxa are encoded by the tree's leaves, or nodes having degree 1. A node of a tree having degree larger than 1 is called an internal node.

Given: A positive integer n (n≤1000) and an adjacency list corresponding to a graph on n nodes that contains no cycles.

Return: The minimum number of edges that can be added to the graph to produce a tree.
Sample Dataset

10
1 2
2 8
4 10
5 9
6 10
7 9

Sample Output

3
'''

FILEPATH = r"TREE_completing_a_tree\data.txt"

def missing_edges(nodes, tuple_list):
    def find(parent, a):
        while parent[a] != a:
            a, parent[a] = parent[a], parent[parent[a]]
        return a
    
    def unite(parent, a, b):
        ra, rb = find(parent, a), find(parent, b)
        if ra != rb:
            parent[ra] = ra
    
    parent = {i: i for i in range(1, nodes + 1)}

    for a, b in tuple_list:
        unite(parent, a, b)

    roots = {find(parent, node) for node in parent}

    return len(roots)

def main():
    with open(FILEPATH) as file:
        data = file.read().strip().split('\n')

    n = int(data[0])
    adjacency_list = [tuple(map(int, line.split())) for line in data[1:]]

    print(missing_edges(n, adjacency_list))
    
if __name__ == "__main__":
    main()