'''
Problem

A circular string is a string that does not have an initial or terminal element; instead, the string is viewed as a necklace of symbols. We can represent a circular string as a string enclosed in parentheses. For example, consider the circular DNA string (ACGTAC), and note that because the string "wraps around" at the end, this circular string can equally be represented by (CGTACA), (GTACAC), (TACACG), (ACACGT), and (CACGTA). The definitions of substrings and superstrings are easy to generalize to the case of circular strings (keeping in mind that substrings are allowed to wrap around).

Given: A collection of (error-free) DNA k-mers (k≤50) taken from the same strand of a circular chromosome. In this dataset, all k-mers from this strand of the chromosome are present, and their de Bruijn graph consists of exactly one simple cycle.

Return: A cyclic superstring of minimal length containing the reads (thus corresponding to a candidate cyclic chromosome).
Sample Dataset

ATTAC
TACAG
GATTA
ACAGA
CAGAT
TTACA
AGATT

Sample Output

GATTACA
'''

FILEPATH = r"PCOV_genome_assembly_with_perfect_coverage\data.txt"

def main():
    with open(FILEPATH) as file:
        kmers = file.read().strip().splitlines()

    l_k = len(kmers)
    start = kmers[0]
    base_length = len(start)

    prefix_map = {kmer[:(base_length - 1):]: kmer for kmer in kmers}

    result = [start]
    current = start
    for _ in range(l_k - 1):
        suffix = current[1:]
        following = prefix_map[suffix]
        result.append(following[-2])
        current = following

    seed = "".join(result)
    print(seed[:l_k])  

if __name__ == "__main__":
    main()