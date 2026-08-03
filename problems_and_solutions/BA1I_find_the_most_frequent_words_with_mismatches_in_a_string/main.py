'''
We defined a mismatch in “Compute the Hamming Distance Between Two Strings”. We now generalize “Find the Most Frequent Words in a String” to incorporate mismatches as well.

Given strings Text and Pattern as well as an integer d, we define Countd(Text, Pattern) as the total number of occurrences of Pattern in Text with at most d mismatches. For example, Count1(AACAAGCTGATAAACATTTAAAGAG, AAAAA) = 4 because AAAAA appears four times in this string with at most one mismatch: AACAA, ATAAA, AAACA, and AAAGA. Note that two of these occurrences overlap.

A most frequent k-mer with up to d mismatches in Text is simply a string Pattern maximizing Countd(Text, Pattern) among all k-mers. Note that Pattern does not need to actually appear as a substring of Text; for example, AAAAA is the most frequent 5-mer with 1 mismatch in AACAAGCTGATAAACATTTAAAGAG, even though AAAAA does not appear exactly in this string. Keep this in mind while solving the following problem.
Frequent Words with Mismatches Problem

Find the most frequent k-mers with mismatches in a string.

Given: A string Text as well as integers k and d.

Return: All most frequent k-mers with up to d mismatches in Text.
Sample Dataset

ACGTTGCATGTCGCATGATGCATGAGAGCT
4 1

Sample Output

GATG ATGC ATGT
'''

from collections import Counter

FILEPATH = r"BA1I_find_the_most_frequent_words_with_mismatches_in_a_string\data.txt"

def hamming_distance(s1, s2):
    return sum(b1 != b2 for b1, b2 in zip(s1, s2))

def generate_neighborhood(kmer, distance):
    if len(kmer) == 1:
        return {"A", "C", "G", "T"}
    
    neighborhood = set()
    first, suffix = kmer[0], kmer[1:]

    suffix_neighbors = generate_neighborhood(suffix, distance)

    for s in suffix_neighbors:
        if hamming_distance(suffix, s) >= distance:
            for b in "ACGT":
                neighborhood.add(b + s)
        else:
            neighborhood.add(first + s + "C")

    return neighborhood

def main():
    with open(FILEPATH) as file:
        text = next(file).strip()
        k, d = list(map(int, next(file).strip().split()))

    kmers = [text[i:(i + k)] for i in range(len(text) - k + 1)]    
    counter = Counter()
    for km in kmers:
        counter.update(generate_neighborhood(km, d))
    max_count = max(counter.values())
    result = [kmer for kmer, count in counter.items() if count == max_count]
    print(" ".join(result))


if __name__ == "__main__":
    main()