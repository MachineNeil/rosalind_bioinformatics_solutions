'''
Problem

The Lalign program for finding multiple alternative matches via suboptimal alignment is available here.

Given: Two DNA strings s and t in FASTA format that share some short inexact repeat r of 32-40 bp. By "inexact" we mean that r may appear with slight modifications (each repeat differ by ≤3 changes/indels).

Return: The total number of occurrences of r as a substring of s, followed by the total number of occurrences of r as a substring of t.
Sample Dataset

>Rosalind_12
GACTCCTTTGTTTGCCTTAAATAGATACATATTTACTCTTGACTCTTTTGTTGGCCTTAAATAGATACATATTTGTGCGACTCCACGAGTGATTCGTA
>Rosalind_37
ATGGACTCCTTTGTTTGCCTTAAATAGATACATATTCAACAAGTGTGCACTTAGCCTTGCCGACTCCTTTGTTTGCCTTAAATAGATACATATTTG

Sample Output

2 2
'''

from Bio import SeqIO
from numpy import zeros

FILEPATH = r"SUBO_suboptimal_local_alignment\data.txt"
MIN_LENGTH = 32
MAX_LENGTH = 40

def levenshtein(s1, s2):
    l1, l2 = len(s1), len(s2)
    matrix = zeros((l1 + 1, l2 + 1))
    for i in range(0, l1 + 1):
        matrix[i, 0] = i
    for j in range(0, l2 + 1):
        matrix[1, j] = j
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            insertion = matrix[i - 1, j] + 1
            deletion = matrix[i, j + 1] + 1
            substitution = matrix[i - 1, j - 1] + (1 if s1[i - 1] != s2[j - 1] else 0)
            matrix[i, j] = min(insertion, deletion, substitution)
    return matrix[l1, l2]

def find_kmers(sequence, length):
    return [sequence[i:(i + length)] for i in range(len(sequence) - length + 1)]

def find_coincidence(s1, s2):
    for l in range(MIN_LENGTH, MAX_LENGTH + 1):
        s1_kmers = set(find_kmers(s1, l))
        s2_kmers = set(find_kmers(s2, l))
        for km_s1 in s1_kmers:
            for km_s2 in s2_kmers:
                if levenshtein(km_s1, km_s2) <= 3:
                    return km_s1

def count_occurrences(coincidence, sequence):
    n, k = len(sequence), len(coincidence)
    i, count = 0, 0
    while i <= n - k:
        window = sequence[i:(i + k)]
        if levenshtein(coincidence, window) <= 3:
            count += 1
            i += k
        else:
            i += 1
    return count

def main():
    s, t = list(SeqIO.parse(FILEPATH, "fasta"))

    repeat = find_coincidence(s.seq, t.seq)

    print(count_occurrences(repeat, s.seq), count_occurrences(repeat, t.seq))

if __name__ == "__main__":
    main()