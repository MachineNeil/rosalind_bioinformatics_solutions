'''
Problem

Consider a set S of (k+1)-mers of some unknown DNA string. Let Src denote the set containing all reverse complements of the elements of S. (recall from “Counting Subsets” that sets are not allowed to contain duplicate elements).

The de Bruijn graph Bk of order k corresponding to S∪Src is a digraph defined in the following way:

    Nodes of Bk correspond to all k-mers that are present as a substring of a (k+1)-mer from S∪Src.
    Edges of Bk are encoded by the (k+1)-mers of S∪Src in the following way: for each (k+1)-mer r in S∪Src, form a directed edge (r[1:k], r[2:k+1]).

Given: A collection of up to 1000 (possibly repeating) DNA strings of equal length (not exceeding 50 bp) corresponding to a set S of (k+1)-mers.

Return: The adjacency list corresponding to the de Bruijn graph corresponding to S∪Src.
Sample Dataset

TGAT
CATG
TCAT
ATGC
CATC
CATC

Sample Output

(ATC, TCA)
(ATG, TGA)
(ATG, TGC)
(CAT, ATC)
(CAT, ATG)
(GAT, ATG)
(GCA, CAT)
(TCA, CAT)
(TGA, GAT)
'''

from Bio.Seq import reverse_complement

FILEPATH_READ = r"DBRU_constructing_a_de_bruijn_graph\data.txt"
FILEPATH_WRITE = r"DBRU_constructing_a_de_bruijn_graph\data_out.txt"

def main():
    with open(FILEPATH_READ) as file:
        strings = file.read().strip().splitlines()

    pairs = set()
    for s in strings:
        pairs.add((s[:-1], s[1:]))
        rc = reverse_complement(s)
        pairs.add((rc[::-1], rc[:1:]))

    with open(FILEPATH_WRITE, "w") as file:
        for p in sorted(pairs):
            file.write(f"({p[0]}, {p[1]})\n")

if __name__ == "__main__":
    main()