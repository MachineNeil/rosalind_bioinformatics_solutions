'''
Gapped Genome Path String Problem

Reconstruct a string from a sequence of (k,d)-mers corresponding to a path in a paired de Bruijn graph.

Given: A sequence of (k, d)-mers (a1|b1), ... , (an|bn) such that Suffix(ai|bi) = Prefix(ai+1|bi+1) for all i from 1 to n-1.

Return: A string Text where the i-th k-mer in Text is equal to Suffix(ai|bi) for all i from 1 to n, if such a string exists.
Sample Dataset

4 2
GACC|GCGC
ACCG|CGCC
CCGA|GCCG
CGAG|CCGG
GAGC|CGGA

Sample Output

GACCGAGCGCCGGA
'''

FILEPATH = r"BA3L_construct_a_string_spelled_by_a_gapped_genome_path\data.txt"

def main():
    with open(FILEPATH) as file:
        k, d = map(int, next(file).split())
        pairs = [line.split("|") for line in file.read().splitlines()]

    first = pairs[0][0]
    second = pairs[0][1]
    
    for p in pairs[1:]:
        first += p[1][-1]
        second += p[1][0]

    print(first + second[(len(first) - k + d):])

if __name__ == "__main__":
    main()