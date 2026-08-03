'''
Problem
Figure 2. Palindromic recognition site

A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC. See Figure 2.

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.
Sample Dataset

>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT

Sample Output

4 6
5 4
6 6
7 4
17 4
18 4
20 6
21 4
'''

from Bio import SeqIO
from Bio.Seq import reverse_complement

FILEPATH = r"REVP_locating_restriction_sites\data.txt"
MIN_LENGTH = 4
MAX_LENGTH = 12

def main():
    sequence = next(SeqIO.parse(FILEPATH, "fasta")).seq

    for j in range(len(sequence)):
        for i in range(MIN_LENGTH, MAX_LENGTH + 1):
            if j > len(sequence):
                break
            string = sequence[j:(j + i)]
            if string == reverse_complement(string):
                print(j + 1, i)

if __name__ == "__main__":
    main()