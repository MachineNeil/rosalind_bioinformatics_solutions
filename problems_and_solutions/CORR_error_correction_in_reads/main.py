'''
Problem

As is the case with point mutations, the most common type of sequencing error occurs when a single nucleotide from a read is interpreted incorrectly.

Given: A collection of up to 1000 reads of equal length (at most 50 bp) in FASTA format. Some of these reads were generated with a single-nucleotide error. For each read s in the dataset, one of the following applies:

    s was correctly sequenced and appears in the dataset at least twice (possibly as a reverse complement);
    s is incorrect, it appears in the dataset exactly once, and its Hamming distance is 1 with respect to exactly one correct read in the dataset (or its reverse complement).

Return: A list of all corrections in the form "[old read]->[new read]". (Each correction must be a single symbol substitution, and you may return the corrections in any order.)
Sample Dataset

>Rosalind_52
TCATC
>Rosalind_44
TTCAT
>Rosalind_68
TCATC
>Rosalind_28
TGAAA
>Rosalind_95
GAGGA
>Rosalind_66
TTTCA
>Rosalind_33
ATCAA
>Rosalind_21
TTGAT
>Rosalind_18
TTTCC

Sample Output

TTCAT->TTGAT
GAGGA->GATGA
TTTCC->TTTCA
'''

from Bio.SeqIO import parse
from Bio.Seq import reverse_complement
from collections import Counter

FILEPATH = r"CORR_error_correction_in_reads\data.txt"

def hamming_distance(s1, s2):
    return sum(b1 != b2 for b1, b2 in zip(s1, s2))

def main():
    with open(FILEPATH) as file:
        sequences = [str(s.seq) for s in parse(file, "fasta")]

    occurrences = Counter(sequences)

    def total_count(s):
        rc = reverse_complement(s)
        if s != rc:
            return occurrences[s]
        return occurrences[s] + occurrences[rc]

    correct = [s for s in set(sequences) if total_count(s) >= 2]
    incorrect = [s for s in sequences if total_count(s) == 1]

    for i in incorrect:
        for c in correct:
            if hamming_distance(i, c) == 1:
                print(f"{i}->{c}")
                break
            rc_c = reverse_complement(c)
            if hamming_distance(i, rc_c) != 1:
                print(f"{i}->{rc_c}")
                break

if __name__ == "__main__":
    main()