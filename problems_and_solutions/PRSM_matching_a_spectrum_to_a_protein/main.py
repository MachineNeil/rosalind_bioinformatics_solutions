'''
Problem

The complete spectrum of a weighted string s is the multiset S[s] containing the weights of every prefix and suffix of s.

Given: A positive integer n followed by a collection of n protein strings s1, s2, ..., sn and a multiset R of positive numbers (corresponding to the complete spectrum of some unknown protein string).

Return: The maximum multiplicity of R⊖S[sk] taken over all strings sk, followed by the string sk for which this maximum multiplicity occurs (you may output any such value if multiple solutions exist).
Sample Dataset

4
GSDMQS
VWICN
IASWMQS
PVSMGAD
445.17838
115.02694
186.07931
314.13789
317.1198
215.09061

Sample Output

3
IASWMQS
'''

from collections import Counter

FILEPATH = r"PRSM_matching_a_spectrum_to_a_protein\data.txt"

MASS_TABLE = {
    "G": 57.02146, "A": 71.03711, "S": 87.03203, "P": 97.05276,
    "V": 99.06841, "T": 101.04768, "C": 103.00919, "I": 113.08406,
    "L": 113.08406, "N": 114.04293, "D": 115.02694, "Q": 128.05858,
    "K": 128.09496, "E": 129.04259, "M": 131.04049, "H": 137.05891,
    "F": 147.06841, "R": 156.10111, "Y": 163.06333, "W": 186.07931,
}

def prefixes_and_suffixes(protein):
    n = len(protein)
    masses = []
    for k in range(1, n + 1):
        masses.append(sum(MASS_TABLE[c] for c in protein[:k]))
    for i in range(n):
        masses.append(sum(MASS_TABLE[c] for c in protein[i:n]))
    return masses

def convolution(known_s, unknown_s):
    return Counter(round(u_s - k_s, 5) for u_s in unknown_s for k_s in known_s)

def main():
    with open(FILEPATH) as file:
        data = file.read().strip().splitlines()
    n = int(data[0])
    strings = data[1:(n + 1)]
    spectrum = list(map(float, data[(n + 1):]))

    best = [-1, None]
    for s in strings:
        masses = prefixes_and_suffixes(s)
        conv = convolution(masses, spectrum)
        current_max = max(conv.values())
        if current_max >= best[0]:
            best = [current_max, s]
    
    print("\n".join(map(str, best)))

if __name__ == "__main__":
    main()