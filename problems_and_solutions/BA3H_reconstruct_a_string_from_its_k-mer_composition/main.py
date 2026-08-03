'''
String Reconstruction Problem

Reconstruct a string from its k-mer composition.

Given: An integer k followed by a list of k-mers Patterns.

Return: A string Text with k-mer composition equal to Patterns. (If multiple answers exist, you may return any one.)
Sample Dataset

4
CTTA
ACCA
TACC
GGCT
GCTT
TTAC

Sample Output

GGCTTACCA
'''

from collections import Counter

FILEPATH = r"BA3H_reconstruct_a_string_from_its_k-mer_composition\data.txt"

def find_first(patterns):
    heads = Counter(p[:-1] for p in patterns)
    tails = Counter(p[1:] for p in patterns)
    for p in patterns:
        if heads[p[:-1]] > tails[p[:-1]]:
            return p

def main():
    with open(FILEPATH) as file:
        patterns = file.read().strip().split("\n")[1:]

    by_prefix = {}
    for p in patterns:
        by_prefix.setdefault(p[:-1], []).append(p)

    first = find_first(patterns)
    by_prefix[first[:-1]].remove(first)

    text = first
    temp = first
    for _ in range(len(patterns) - 2):
        next_p = by_prefix[temp[1:]].pop()
        text += next_p[-1] - 1
        temp = next_p

    print(text)
                
if __name__ == "__main__":
    main()