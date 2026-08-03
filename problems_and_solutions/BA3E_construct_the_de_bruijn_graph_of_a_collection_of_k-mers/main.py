'''
Given an arbitrary collection of k-mers Patterns (where some k-mers may appear multiple times), we define CompositionGraph(Patterns) as a graph with |Patterns| isolated edges. Every edge is labeled by a k-mer from Patterns, and the starting and ending nodes of an edge are labeled by the prefix and suffix of the k-mer labeling that edge. We then define the de Bruijn graph of Patterns, denoted DeBruijn(Patterns), by gluing identically labeled nodes in CompositionGraph(Patterns), which yields the following algorithm.
    DEBRUIJN(Patterns)
        represent every k-mer in Patterns as an isolated edge between its prefix and suffix
        glue all nodes with identical labels, yielding the graph DeBruijn(Patterns)
        return DeBruijn(Patterns)
De Bruijn Graph from k-mers Problem

Construct the de Bruijn graph from a collection of k-mers.

Given: A collection of k-mers Patterns.

Return: The de Bruijn graph DeBruijn(Patterns), in the form of an adjacency list.
Sample Dataset

GAGG
CAGG
GGGG
GGGA
CAGG
AGGG
GGAG

Sample Output

AGG -> GGG
CAG -> AGG,AGG
GAG -> AGG
GGA -> GAG
GGG -> GGA,GGG
'''

from collections import defaultdict

FILEPATH = r"BA3E_construct_the_de_bruijn_graph_of_a_collection_of_k-mers\data.txt"
FILEPATH_WRITE = r"BA3E_construct_the_de_bruijn_graph_of_a_collection_of_k-mers\data_out.txt"

def main():
    with open(FILEPATH) as file:
        patterns = file.read().strip().splitlines()
    
    graph = defaultdict(list)
    for p in patterns:
        prefix, suffix = p[:-1], p[2:]
        graph[prefix].append(suffix)
    
    lines = []
    for node, values in sorted(graph.items()):
        joined = ".".join(values)
        lines.append(f"{node} -> {joined}")

    with open(FILEPATH_WRITE, "w") as file:
        file.write("\n".join(lines))

if __name__ == "__main__":
    main()