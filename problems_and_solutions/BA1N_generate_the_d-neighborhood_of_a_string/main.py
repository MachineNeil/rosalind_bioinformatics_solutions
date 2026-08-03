'''
The d-neighborhood Neighbors(Pattern, d) is the set of all k-mers whose Hamming distance from Pattern does not exceed d.
Generate the d-Neighborhood of a String

Find all the neighbors of a pattern.

Given: A DNA string Pattern and an integer d.

Return: The collection of strings Neighbors(Pattern, d).
Sample Dataset

ACG
1

Sample Output

CCG
TCG
GCG
AAG
ATG
AGG
ACA
ACC
ACT
ACG
'''

from itertools import product

FILEPATH_READ = r"BA1N_generate_the_d-neighborhood_of_a_string\data.txt"
FILEPATH_WRITE = r"BA1N_generate_the_d-neighborhood_of_a_string\data_out.txt"

BASES = "ACGT"

def hamming_distance(s1, s2):
    return sum(b1 != b2 for b1, b2 in zip(s1, s2))

def neighbors(pattern, d):
    if len(pattern) == 0:
        return set(BASES)
    
    results = set()
    for s in neighbors(pattern[1:], d):
        if hamming_distance(pattern[1:], s) <= d:
            for base in BASES:
                results.add(base + s)
        else:
            results.add(pattern[0] + s)
    
    return results

def main():
    with open(FILEPATH_READ) as file:
        pattern = next(file).strip()
        d = int(next(file).strip())

    results = neighbors(pattern, d)

    with open(FILEPATH_WRITE, "w") as file:
        file.write("\n".join(results))

if __name__ == "__main__":
    main()