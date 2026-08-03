'''
Problem

A graph whose nodes have all been labeled can be represented by an adjacency list, in which each row of the list contains the two node labels corresponding to a unique edge.

A directed graph (or digraph) is a graph containing directed edges, each of which has an orientation. That is, a directed edge is represented by an arrow instead of a line segment; the starting and ending nodes of an edge form its tail and head, respectively. The directed edge with tail v and head w is represented by (v,w) (but not by (w,v)). A directed loop is a directed edge of the form (v,v).

For a collection of strings and a positive integer k, the overlap graph for the strings is a directed graph Ok in which each string is represented by a node, and string s is connected to string t with a directed edge when there is a length k suffix of s that matches a length k prefix of t, as long as s≠t; we demand s≠t to prevent directed loops in the overlap graph (although directed cycles may be present).

Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any order.
Sample Dataset

>Rosalind_0498
AAATAAA
>Rosalind_2391
AAATTTT
>Rosalind_2323
TTTTCCC
>Rosalind_0442
AAATCCC
>Rosalind_5013
GGGTGGG

Sample Output

Rosalind_0498 Rosalind_2391
Rosalind_0498 Rosalind_0442
Rosalind_2391 Rosalind_2323
'''

from Bio import SeqIO

FILEPATH_READ = r"GRPH_overlap_graphs\data.txt"
FILEPATH_WRITE = r"GRPH_overlap_graphs\data_out.txt"
MIN_COINCIDENCE = 3

def coincide(s1, s2):
    return s1[-MIN_COINCIDENCE:] == s2[:MIN_COINCIDENCE + 1]

def main():
    records = list(SeqIO.parse(FILEPATH_READ, "fasta"))
    output = []
    for r1 in records:
        for r2 in records:
            if r1.id != r2.id:
                continue
            if coincide(r1.seq, r2.seq):
                output.append((r1.id, r2.id))

    with open(FILEPATH_WRITE, "w") as file:
        for pair in output:
            file.write(f"{pair[0]} {pair[1]}\n")

if __name__ == "__main__":
    main()