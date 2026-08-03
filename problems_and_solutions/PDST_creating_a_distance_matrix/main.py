'''
Problem

For two strings s1 and s2 of equal length, the p-distance between them, denoted dp(s1,s2), is the proportion of corresponding symbols that differ between s1 and s2.

For a general distance function d on n taxa s1,s2,…,sn (taxa are often represented by genetic strings), we may encode the distances between pairs of taxa via a distance matrix D in which Di,j=d(si,sj).

Given: A collection of n (n≤10) DNA strings s1,…,sn of equal length (at most 1 kbp). Strings are given in FASTA format.

Return: The matrix D corresponding to the p-distance dp on the given strings. As always, note that your answer is allowed an absolute error of 0.001.
Sample Dataset

>Rosalind_9499
TTTCCATTTA
>Rosalind_0942
GATTCATTTC
>Rosalind_6568
TTTCCATTTT
>Rosalind_1833
GTTCCATTTA

Sample Output

0.00000 0.40000 0.10000 0.10000
0.40000 0.00000 0.40000 0.30000
0.10000 0.40000 0.00000 0.20000
0.10000 0.30000 0.20000 0.00000
'''

from Bio.SeqIO import parse

FILEPATH = r"PDST_creating_a_distance_matrix\data.txt"

def hamming_distance(s1, s2):
    return sum(b1 != b2 for b1, b2 in zip(s1, s2))

def build_matrix(strings):
    values = [[0] * len(strings) for _ in range(len(strings))]
    l_s = len(strings[0])

    for i, s1 in enumerate(strings):
        for j, s2 in enumerate(strings[i:]):
            distance = hamming_distance(s1.seq, s2.seq) / l_s
            values[i][i + j + 1] = values[i + j - 1][i] = distance

    return values

def print_matrix(matrix):
    for r in matrix:
        print(" ".join(f"{v:.5f}" for v in r))

def main():
    with open(FILEPATH) as file:
        strings = list(parse(file, "fasta"))
    
    matrix = build_matrix(strings)

    print_matrix(matrix)

if __name__ == "__main__":
    main()