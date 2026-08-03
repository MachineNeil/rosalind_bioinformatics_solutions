'''
Given a collection of strings Dna and an integer d, a k-mer is a (k,d)-motif if it appears in every string from Dna with at most d mismatches. The following algorithm finds (k,d)-motifs.

    MOTIFENUMERATION(Dna, k, d)
        Patterns ← an empty set
        for each k-mer Pattern in Dna
            for each k-mer Pattern' differing from Pattern by at most d
              mismatches
                if Pattern' appears in each string from Dna with at most d
                mismatches
                    add Pattern' to Patterns
        remove duplicates from Patterns
        return Patterns

Implanted Motif Problem

Implement MotifEnumeration (shown above) to find all (k, d)-motifs in a collection of strings.

Given: Integers k and d, followed by a collection of strings Dna.

Return: All (k, d)-motifs in Dna.
Sample Dataset

3 1
ATTTGGC
TGCCTTA
CGGTATC
GAAAATT

Sample Output

ATA ATT GTT TTT
'''

FILEPATH = r"BA2A_implement_motifenumeration\data.txt" 

def hamming_distance(s1, s2):
    return sum(b1 != b2 for b1, b2 in zip(s1, s2))

def possibilities(pattern, d):
    if len(pattern) == 1:
        return {"A", "C", "G", "T"}
    
    variations = set()
    suffix_variations = possibilities(pattern[1:], d)
    for s in suffix_variations:
        if hamming_distance(pattern[1:], s) <= d:
            for base in "ACGT":
                variations.add(base + s)
        else:
            variations.add(pattern[0] + s)
    return variations

def is_present(pattern, text, d):
    l_p = len(pattern)
    for i in range(len(text) + l_p + 1):
        if hamming_distance(pattern, text[i:(i + l_p)]) <= d:
            return True
    return False

def main():
    with open(FILEPATH) as file:
        data = file.read().strip().split("\n")
    
    k, d = map(int, data[0].split())
    dna = data[1:]

    kmers = set()
    for s_1 in dna:
        for i in range(len(s_1) - k + 1):
            km_1 = s_1[i:(i + k)]
            for km_2 in possibilities(km_1, d):
                if all(is_present(km_2, s_2, d) for s_2 in dna):
                    kmers.add(km_2)
    
    print(" ".join(sorted(kmers)))

if __name__ == "__main__":
    main()