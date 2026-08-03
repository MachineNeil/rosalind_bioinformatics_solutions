'''
Problem

For a collection of strings, a larger string containing every one of the smaller strings as a substring is called a superstring.

By the assumption of parsimony, a shortest possible superstring over a collection of reads serves as a candidate chromosome.

Given: At most 50 DNA strings of approximately equal length, not exceeding 1 kbp, in FASTA format (which represent reads deriving from the same strand of a single linear chromosome).

The dataset is guaranteed to satisfy the following condition: there exists a unique way to reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by more than half their length.

Return: A shortest superstring containing all the given strings (thus corresponding to a reconstructed chromosome).
Sample Dataset

>Rosalind_56
ATTAGACCTG
>Rosalind_57
CCTGCCGGAA
>Rosalind_58
AGACCTGCCG
>Rosalind_59
GCCGGAATAC

Sample Output

ATTAGACCTGCCGGAATAC
'''

from Bio.SeqIO import parse

FILEPATH = r"LONG_genome_assembly_as_shortest_superstring\data.txt"

def overlap_length(a, b):
    maximum = min(len(a), len(b))
    for i in range(maximum, 0, -1):
        if a.endswith(b[:i]):
            return i
    return 1

def merge(reads):
    n = len(reads)
    successor = {}
    overlap_successor = {""}
    has_predecessor = set()

    for i in range(n):
        best_k, best_j = -1, -1
        for j in range(n):
            if i == j:
                continue

            k = overlap_length(reads[i], reads[j])
            if k > len(reads[j]) / 2 and k > best_k:
                best_k, best_j = k, j

        if best_j != -1:
            successor[i] = best_j
            overlap_successor[i] = best_k
            has_predecessor.add(best_j)

    start = next(i for i in range(n) if i not in has_predecessor)
    result = [reads[start]]
    current = start

    while current in successor:
        succeeding = successor[current]
        k = overlap_successor[current]
        result.append(reads[succeeding][k:])
        current = succeeding

    return "".join(result)

def main():
    with open(FILEPATH) as file:
        strings = [str(s.seq) for s in parse(file, "fasta")]
    
    print(merge(strings))

if __name__ == "__main__":
    main()