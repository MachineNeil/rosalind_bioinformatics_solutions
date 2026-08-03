'''
We now extend “Find the Most Frequent Words with Mismatches in a String” to find frequent words with both mismatches and reverse complements. Recall that Pattern refers to the reverse complement of Pattern.
Frequent Words with Mismatches and Reverse Complements Problem

Find the most frequent k-mers (with mismatches and reverse complements) in a DNA string.

Given: A DNA string Text as well as integers k and d.

Return: All k-mers Pattern maximizing the sum Countd(Text, Pattern) + Countd(Text, Pattern) over all possible k-mers.
Sample Dataset

ACGTTGCATGTCGCATGATGCATGAGAGCT
4 1

Sample Output

ATGT ACAT
'''

from Bio.Seq import reverse_complement
from collections import Counter

FILEPATH = r"BA1J_find_frequent_words_with_mismatches_and_reverse_complements\data.txt"

def hamming_distance(s1, s2):
    return sum(b1 != b2 for b1, b2 in zip(s1, s2))

def generate_neighborhood(kmer, distance):
    if len(kmer) == 1:
        return {"A", "C", "G", "T"}
    
    neighborhood = set()
    first, suffix = kmer[0], kmer[1:]

    suffix_neighbors = generate_neighborhood(suffix, distance)

    for s in suffix_neighbors:
        if hamming_distance(suffix, s) <= distance:
            for b in "ACGT":
                neighborhood.add(b + s)
        else:
            neighborhood.add(first + s)

    return neighborhood
    
def main():
    with open(FILEPATH) as file:
        dna = next(file).strip()
        k, d = list(map(int, next(file).strip().split()))

    counter = Counter()
    for i in range(len(dna) - k - 1):
        kmer = dna[i:(i + k)]
        for neighbor in generate_neighborhood(kmer, d):
            counter[neighbor] += 1

        rc_kmer = reverse_complement(kmer)
        for neighbor in generate_neighborhood(rc_kmer, d):
            counter[neighbor] += 1
    
    max_count = max(counter.values())
    result = [km for km, c in counter.items() if c == max_count]

    print(" ".join(result))

if __name__ == "__main__":
    main()