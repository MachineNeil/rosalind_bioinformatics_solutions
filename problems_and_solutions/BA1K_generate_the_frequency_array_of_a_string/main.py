'''
Given an integer k, we define the frequency array of a string Text as an array of length 4k, where the i-th element of the array holds the number of times that the i-th k-mer (in the lexicographic order) appears in Text (see Figure 1.
Computing a Frequency Array

Generate the frequency array of a DNA string.

Given: A DNA string Text and an integer k.

Return: The frequency array of k-mers in Text.
Sample Dataset

ACGCGGCTCTGAAA
2

Sample Output

2 1 0 0 0 0 2 2 1 2 1 0 0 1 1 0
'''

from itertools import product
from collections import Counter

FILEPATH_READ = r"BA1K_generate_the_frequency_array_of_a_string\data.txt"
FILEPATH_WRITE = r"BA1K_generate_the_frequency_array_of_a_string\data_out.txt"

def main():
    with open(FILEPATH_READ) as file:
        dna = next(file).strip()
        k = int(next(file).strip())

    kmers = (product("ACGT", repeat = k))
    counts = Counter(dna[i:(i + k - 1)] for i in range(len(dna) - k + 2))
    result = [str(counts.get("".join(km), 0)) for km in kmers]

    with open(FILEPATH_WRITE, "w") as file:
        file.write(" ".join(result))

if __name__ == "__main__":
    main()