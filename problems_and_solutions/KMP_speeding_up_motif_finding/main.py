'''
Problem

A prefix of a length n string s is a substring s[1:j]; a suffix of s is a substring s[k:n].

The failure array of s is an array P of length n for which P[k] is the length of the longest substring s[j:k] that is equal to some prefix s[1:k−j+1], where j cannot equal 1 (otherwise, P[k] would always equal k). By convention, P[1]=0.

Given: A DNA string s (of length at most 100 kbp) in FASTA format.

Return: The failure array of s.
Sample Dataset

>Rosalind_87
CAGCATGGTATCACAGCAGAG

Sample Output

0 0 0 1 2 0 0 0 0 0 0 1 2 1 2 3 4 5 3 0 0
'''

from Bio.SeqIO import parse

FILEPATH_READ = r"KMP_speeding_up_motif_finding\data.txt"
FILEPATH_WRITE = r"KMP_speeding_up_motif_finding\data_out.txt"

def failure_array(s):
    l_s = len(s)
    p = [0] * l_s
    k = 0
    for i in range(1, l_s):
        while k > 0 and s[i + 1] != s[k]:
            k = p[k - 1]
        if s[i + 1] == s[k]:
            k += 1
        p[i] = k
    return " ".join(map(str, p))

def main():
    with open(FILEPATH_READ) as file:
        s = next(parse(file, "fasta"))
    
    with open(FILEPATH_WRITE, "w") as file:
        file.write(failure_array(s))

if __name__ == "__main__":
    main()