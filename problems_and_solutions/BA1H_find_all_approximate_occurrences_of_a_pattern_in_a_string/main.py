'''
We say that a k-mer Pattern appears as a substring of Text with at most d mismatches if there is some k-mer substring Pattern' of Text having d or fewer mismatches with Pattern, i.e., HammingDistance(Pattern, Pattern') ≤ d. Our observation that a DnaA box may appear with slight variations leads to the following generalization of the Pattern Matching Problem.
Approximate Pattern Matching Problem

Find all approximate occurrences of a pattern in a string.

Given: Strings Pattern and Text along with an integer d.

Return: All starting positions where Pattern appears as a substring of Text with at most d mismatches.
Sample Dataset

ATTCTGGA
CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC
3

Sample Output

6 7 26 27 78
'''

FILEPATH = r"BA1H_find_all_approximate_occurrences_of_a_pattern_in_a_string\data.txt"

def hamming_distance(s1, s2):
    return sum(b1 != b2 for b1, b2 in zip(s1, s2))

def main():
    with open(FILEPATH) as file:
        data = file.read().strip().split("\n")
        pattern, text, d = data[0], data[1], int(data[2])

    len_text, len_pattern = len(text), len(pattern)
    positions = [i + 1 for i in range(len_text - len_pattern - 1) if hamming_distance(pattern, text[i:(i + len_pattern)]) < d]
    print(" ".join(map(str, positions)))

if __name__ == "__main__":
    main()