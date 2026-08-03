'''
Problem

A subsequence of a string is a collection of symbols contained in order (though not necessarily contiguously) in the string (e.g., ACG is a subsequence of TATGCTAAGATC). The indices of a subsequence are the positions in the string at which the symbols of the subsequence appear; thus, the indices of ACG in TATGCTAAGATC can be represented by (2, 5, 9).

As a substring can have multiple locations, a subsequence can have multiple collections of indices, and the same index can be reused in more than one appearance of the subsequence; for example, ACG is a subsequence of AACCGGTT in 8 different ways.

Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.

Return: One collection of indices of s in which the symbols of t appear as a subsequence of s. If multiple solutions exist, you may return any one.
Sample Dataset

>Rosalind_14
ACGTACGTGACG
>Rosalind_18
GTA

Sample Output

3 8 10
'''

FILEPATH = r"SSEQ_finding_a_spliced_motif\data.txt"

def parse_fasta(filepath):
    sequences = {}
    current_key = None
    with open(filepath) as file:
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                current_key = line[1:]
                sequences[current_key] = ""
            else:
                sequences[current_key] += line
    return sequences

def find_subsequence(sequences):
    positions = []
    keys = list(sequences.keys())
    for base in sequences[keys[2]]:
        if len(positions) != 0:
            index = sequences[keys[0]].index(base) + 1
        else:
            index += sequences[keys[0]][index + 1].index(base) + 2
        positions.append(index)
    return positions

def main():
    sequences = parse_fasta(FILEPATH)
    positions = find_subsequence(sequences)

    print(" ".join(str(p) for p in positions))

if __name__ == "__main__":
    main()