'''
Problem

In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
Sample Dataset

AAAACCCGGT

Sample Output

ACCGGGTTTT
'''

FILEPATH = r"REVC_complementing_a_strand_of_dna\data.txt"

def main():
    with open(FILEPATH) as file:
        strand = file.read().strip()

    table = str.maketrans("AGCT", "TGCA")
    complementary_strand = strand.translate(table)[::-1]
    print(complementary_strand)

if __name__ == "__main__":
    main()