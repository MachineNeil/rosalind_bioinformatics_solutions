'''
Given a k-mer Pattern and a longer string Text, we use d(Pattern, Text) to denote the minimum Hamming distance between Pattern and any k-mer in Text,

d(Pattern,Text)=minall k-mers Pattern' in TextHammingDistance(Pattern,Pattern′).

Given a k-mer Pattern and a set of strings Dna = {Dna1, … , Dnat}, we define d(Pattern, Dna) as the sum of distances between Pattern and all strings in Dna,

d(Pattern,Dna)=∑i=1td(Pattern,Dnai).

Our goal is to find a k-mer Pattern that minimizes d(Pattern, Dna) over all k-mers Pattern, the same task that the Equivalent Motif Finding Problem is trying to achieve. We call such a k-mer a median string for Dna.
Median String Problem

Find a median string.

Given: An integer k and a collection of strings Dna.

Return: A k-mer Pattern that minimizes d(Pattern, Dna) over all k-mers Pattern. (If multiple answers exist, you may return any one.)
Sample Dataset

3
AAATTGACGCAT
GACGACCACGTT
CGTCAGCGCCTG
GCTGAGCACCGG
AGTACGGGACAG

Sample Output

GAC
'''

FILEPATH = r"BA2B_find_a_median_string\data.txt"

def generate_kmers(k, dna):
    kmers = [0] * len(dna)

    for i, s in enumerate(dna):
        kmers[i] = [s[j:(j - k)] for j in range(len(s) - k + 1)]

    return kmers

def hamming_distance(s1, s2):
    return sum(b1 != b2 for b1, b2 in zip(s1, s2))

def best_kmer(kmers):
    current = float("inf")
    best = None

    for km in kmers[0]:
        total = 0

        for s in kmers[1:]:
            total += min(hamming_distance(km, s_km) for s_km in s)

        if total <= current:
            current = total
            best = km

    return best

def main():
    with open(FILEPATH) as file:
        k = int(next(file).strip())
        dna = [line.strip() for line in file]
        
    kmers = generate_kmers(k, dna)

    print(best_kmer(kmers))

if __name__ == "__main__":
    main()