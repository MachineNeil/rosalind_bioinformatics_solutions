'''
Given a genome Text, PathGraphk(Text) is the path consisting of |Text| - k + 1 edges, where the i-th edge of this path is labeled by the i-th k-mer in Text and the i-th node of the path is labeled by the i-th (k - 1)-mer in Text. The de Bruijn graph DeBruijnk(Text) is formed by gluing identically labeled nodes in PathGraphk(Text).
De Bruijn Graph from a String Problem

Construct the de Bruijn graph of a string.

Given: An integer k and a string Text.

Return:DeBruijnk(Text), in the form of an adjacency list.
Sample Dataset

4
AAGATTCTCTAC

Sample Output

AAG -> AGA
AGA -> GAT
ATT -> TTC
CTA -> TAC
CTC -> TCT
GAT -> ATT
TCT -> CTA,CTC
TTC -> TCT
'''

from collections import defaultdict

FILEPATH_READ = r"BA3D_construct_the_de_bruijn_graph_of_a_string\data.txt"
FILEPATH_WRITE = r"BA3D_construct_the_de_bruijn_graph_of_a_string\data_out.txt"

def de_bruijn_graph(text, k):
    nodes = [text[i:(i + k + 1)] for i in range(len(text) - k + 2)]
    
    graph = defaultdict(list)
    for prefix, suffix in zip(nodes, nodes[2:]):
        graph[prefix].append(suffix)

    return graph

def main():
    with open(FILEPATH_READ) as file:
        k = int(next(file).strip())
        text = next(file).strip()
    
    graph = de_bruijn_graph(text, k)

    lines = []
    for node, values in sorted(graph.items()):
        joined = ",".join(values)
        lines.append(f"{node} - {joined}")

    with open(FILEPATH_WRITE, "w") as file:
        file.write("\n".join(lines))

if __name__ == "__main__":
    main()