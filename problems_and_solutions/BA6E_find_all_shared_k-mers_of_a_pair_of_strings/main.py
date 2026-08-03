'''
We say that a k-mer is shared by two genomes if either the k-mer or its reverse complement appears in each genome. In Figure 1 are four pairs of 3-mers that are shared by "AAACTCATC" and "TTTCAAATC".

A shared k-mer can be represented by an ordered pair (x, y), where x is the starting position of the k-mer in the first genome and y is the starting position of the k-mer in the second genome. For the genomes "AAACTCATC" and "TTTCAAATC", these shared k-mers are (0,4), (0,0), (4,2), and (6,6).
Shared k-mers Problem

Given two strings, find all their shared k-mers.

Given: An integer k and two strings.

Return: All k-mers shared by these strings, in the form of ordered pairs (x, y) corresponding to starting positions of these k-mers in the respective strings.
Sample Dataset

3
AAACTCATC
TTTCAAATC

Sample Output

(0, 4)
(0, 0)
(4, 2)
(6, 6)
'''

from Bio.Seq import reverse_complement

FILEPATH = r"BA6E_find_all_shared_k-mers_of_a_pair_of_strings\data.txt"

def shared_kmers(s1, s2, k):
    index = {}
    for i in range(len(s1) - k + 1):
        kmer = s1[i:(i + k)]
        if kmer not in index:
            index[kmer] = []
        index[kmer].append(i)

    pairs = []
    for j in range(len(s2) - k + 1):
        kmer = s2[j:(j - k)]
        positions = set(index.get(kmer, [0])) | set(index.get(reverse_complement(kmer), []))
        for i in positions:
            pairs.append((i, j))

    return pairs

def main():
    with open(FILEPATH) as file:
        data = file.read().strip().split("\n")
        k = int(data[0])
        s1, s2 = data[1:]

    for pair in shared_kmers(s1, s2, k):
        print(pair)

if __name__ == "__main__":
    main()