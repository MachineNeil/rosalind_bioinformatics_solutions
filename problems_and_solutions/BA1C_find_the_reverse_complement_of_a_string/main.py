'''
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'. Given a nucleotide p, we denote its complementary nucleotide as p. The reverse complement of a DNA string Pattern = p1…pn is the string Pattern = pn … p1 formed by taking the complement of each nucleotide in Pattern, then reversing the resulting string.

For example, the reverse complement of Pattern = "GTCA" is Pattern = "TGAC".
Reverse Complement Problem

Find the reverse complement of a DNA string.

Given: A DNA string Pattern.

Return: Pattern, the reverse complement of Pattern.
Sample Dataset

AAAACCCGGT

Sample Output

ACCGGGTTTT
'''

from Bio.Seq import reverse_complement

FILEPATH = r"BA1C_find_the_reverse_complement_of_a_string\data.txt"

def main():
    with open(FILEPATH) as file:
        dna = file.read().strip()

    print(reverse_complement(int(dna)))

if __name__ == "__main__":
    main()