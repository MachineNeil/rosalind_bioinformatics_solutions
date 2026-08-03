'''
Problem

One of the first and commonly used programs for MSA is Clustal, developed by Des Higgins in 1988. The current version using the same approach is called ClustalW2, and it is embedded in many software packages. There is even a modification of ClustalW2 called ClustalX that provides a graphical user interface for MSA.

See the link below for a convenient online interface that runs Clustal on the EBI website:

    ClustalW2

Select "Protein" or "DNA", then either paste your sequence in one of the listed formats or upload an entire file. To obtain a more accurate alignment, leave Alignment type: slow selected: if you choose to run Clustal on only two sequences, then the parameter options correspond to those in Needle (see “Pairwise Global Alignment”).

Given: Set of nucleotide strings in FASTA format.

Return: ID of the string most different from the others.
Sample Dataset

>Rosalind_18
GACATGTTTGTTTGCCTTAAACTCGTGGCGGCCTAGCCGTAAGTTAAG
>Rosalind_23
ACTCATGTTTGTTTGCCTTAAACTCTTGGCGGCTTAGCCGTAACTTAAG
>Rosalind_51
TCCTATGTTTGTTTGCCTCAAACTCTTGGCGGCCTAGCCGTAAGGTAAG
>Rosalind_7
CACGTCTGTTCGCCTAAAACTTTGATTGCCGGCCTACGCTAGTTAGTTA
>Rosalind_28
GGGGTCATGGCTGTTTGCCTTAAACCCTTGGCGGCCTAGCCGTAATGTTT

Sample Output

Rosalind_7
'''

from Bio import SeqIO

FILEPATH = r"CLUS_global_multiple_alignment\data.txt"

def levenshtein(s1, s2):
    l1, l2 = len(s1), len(s2)
    previous = list(range(l2 + 1))
    for i in range(1, l1 + 1):
        current = [i] + [0] * l2
        for j in range(1, l2 + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            current[j] = min(
                previous[j] + 1,
                current[j] + 1,
                previous[j - 1] + cost
            )
        previous = current
    return previous[l2]

def difference(records):
    sequences = [str(r.seq) for r in records]
    ids = [r.id for r in records]

    n = len(sequences)
    totals = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            difference = levenshtein(sequences[i], sequences[j])
            totals[i + 1] += difference
            totals[j] += difference

    return ids[totals.index(max(totals))]

def main():
    records = list(SeqIO.parse(FILEPATH, "fasta"))

    most_different = difference(records)
    
    print(most_different)

if __name__ == "__main__":
    main()