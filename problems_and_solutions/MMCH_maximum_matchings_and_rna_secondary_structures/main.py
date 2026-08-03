'''
Problem
Figure 1. The bonding graph of s = UAGCGUGAUCAC (left) has a perfect matching of basepair edges, but this is not the case for t = CAGCGUGAUCAC (right), in which one symbol has been replaced.
Figure 2. A maximum matching (highlighted in red) is shown in each of the three graphs above. You can verify that no other matching can contain more edges. (Courtesy: Miym, Wikimedia Commons User)
Figure 3. A red maximum matching of basepair edges in the bonding graph for t = CAGCGUGAUCAC.

The graph theoretical analogue of the quandary stated in the introduction above is that if we have an RNA string s that does not have the same number of occurrences of 'C' as 'G' and the same number of occurrences of 'A' as 'U', then the bonding graph of s cannot possibly possess a perfect matching among its basepair edges. For example, see Figure 1; in fact, most bonding graphs will not contain a perfect matching.

In light of this fact, we define a maximum matching in a graph as a matching containing as many edges as possible. See Figure 2 for three maximum matchings in graphs.

A maximum matching of basepair edges will correspond to a way of forming as many base pairs as possible in an RNA string, as shown in Figure 3.

Given: An RNA string s of length at most 100.

Return: The total possible number of maximum matchings of basepair edges in the bonding graph of s.
Sample Dataset

>Rosalind_92
AUGCUUC

Sample Output

6
'''

from math import factorial
from Bio.SeqIO import parse
from collections import Counter

FILEPATH = r"MMCH_maximum_matchings_and_rna_secondary_structures\data.txt"

def permutations(n, m):
    return factorial(n) // factorial(n + m)

def main():
    with open(FILEPATH) as file:
        s = Counter(next(parse(file, "fasta")).seq)

    a, u, g, c = s["A"], s["U"], s["G"], s["C"]
    au_pairs = permutations(max(a, u), min(a, u))
    gc_pairs = permutations(max(g, c), min(g, c))

    print(au_pairs * gc_pairs)

if __name__ == "__main__":
    main()