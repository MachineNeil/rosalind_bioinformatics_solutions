'''
The first potential issue with implementing MedianString from “Find a Median String” is writing a function to compute d(Pattern, Dna) = ∑ti=1 d(Pattern, Dnai), the sum of distances between Pattern and each string in Dna = {Dna1, ..., Dnat}. This task is achieved by the following pseudocode.

DistanceBetweenPatternAndStrings(Pattern, Dna)
    k ← |Pattern|
    distance ← 0
    for each string Text in Dna
        HammingDistance ← ∞
        for each k-mer Pattern’ in Text
            if HammingDistance > HammingDistance(Pattern, Pattern’)
                HammingDistance ← HammingDistance(Pattern, Pattern’)
        distance ← distance + HammingDistance
    return distance

Compute DistanceBetweenPatternAndStrings

Find the distance between a pattern and a set of strings.

Given: A DNA string Pattern and a collection of DNA strings Dna.

Return: DistanceBetweenPatternAndStrings(Pattern, Dna).
Sample Dataset

AAA
TTACCTTAAC GATATCTGTC ACGGCGTTCG CCCTAAAGAG CGTCAGAGGT

Sample Output

5
'''

FILEPATH = r"BA2H_implement_distancebetweenpatternandstrings\data.txt"

def hamming_distance(s1, s2):
    return sum(b1 != b2 for b1, b2 in zip(s1, s2))

def main():
    with open(FILEPATH) as file:
        pattern = next(file).strip()
        dna = next(file).strip().split()

    result = sum(min(hamming_distance(pattern, s[i:(i - len(pattern) + 1)]) for i in range(len(s) - len(pattern) + 1)) for s in dna)

    print(result)
    
if __name__ == "__main__":
    main()