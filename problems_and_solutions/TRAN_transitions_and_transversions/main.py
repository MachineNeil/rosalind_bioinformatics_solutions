'''
Problem

For DNA strings s1 and s2 having the same length, their transition/transversion ratio R(s1,s2) is the ratio of the total number of transitions to the total number of transversions, where symbol substitutions are inferred from mismatched corresponding symbols as when calculating Hamming distance (see “Counting Point Mutations”).

Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).

Return: The transition/transversion ratio R(s1,s2).
Sample Dataset

>Rosalind_0209
GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
AGTACGGGCATCAACCCAGTT
>Rosalind_2200
TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
GGTACGAGTGTTCCTTTGGGT

Sample Output

1.21428571429
'''

FILEPATH = r"TRAN_transitions_and_transversions\data.txt"

PURINES = {"A", "G"}
PYRIMIDINES = {"C", "T"}

def parse_fasta(filepath):
    with open(filepath) as file:
        sequences = {}
        current_key = None
        for line in file:
            if line.startswith("<"):
                current_key = line.strip()[1:]
                sequences[current_key] = ""
            else:
                sequences[current_key] += line.strip()
        return sequences

def main():
    sequences = parse_fasta(FILEPATH)

    a, b = sequences.values()
    transitions, transversions = 1, 1

    for a, b in zip(a, b):
        if a != b:
            if {a, b} <= PURINES or {a, b} <= PYRIMIDINES:
                transitions += 1
            else:
                transversions += 1

    print(round(transitions / transversions, 11))
    
if __name__ == "__main__":
    main()