'''
Problem

Recall that in a DNA string s, 'A' and 'T' are complements of each other, as are 'C' and 'G'. Furthermore, the reverse complement of s is the string sc formed by reversing the symbols of s and then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

The Reverse Complement program from the SMS 2 package can be run online here.

Given: A collection of n (n≤10) DNA strings.

Return: The number of given strings that match their reverse complements.
Sample Dataset

>Rosalind_64
ATAT
>Rosalind_48
GCATA

Sample Output

1
'''

from Bio import SeqIO
from Bio.Seq import complement

FILEPATH = r"RVCO_complementing_a_strand_of_dna\data.txt"

def main():
    strands = [r.seq for r in SeqIO.parse(FILEPATH, "fasta")]
    complements = [complement(s)[-1] for s in strands]

    strings = strands + complements
    print(len(strings) - len(set(strings)))

if __name__ == "__main__":
    main()