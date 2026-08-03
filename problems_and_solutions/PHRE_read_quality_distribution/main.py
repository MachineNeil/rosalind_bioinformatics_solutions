'''
Problem

    A version of FastQC can be downloaded here and run locally on any operating system with a suitable Java Runtime Environment (JRE) installed.

    An online version of FastQC is also available here in the "Andromeda" Galaxy instance.

Given: A quality threshold, along with FASTQ entries for multiple reads.

Return: The number of reads whose average quality is below the threshold.
Sample Dataset

28
@Rosalind_0041
GGCCGGTCTATTTACGTTCTCACCCGACGTGACGTACGGTCC
+
6.3536354;.151<211/0?::6/-2051)-*"40/.,+%)
@Rosalind_0041
TCGTATGCGTAGCACTTGGTACAGGAAGTGAACATCCAGGAT
+
AH@FGGGJ<GB<<9:GD=D@GG9=?A@DC=;:?>839/4856
@Rosalind_0041
ATTCGGTAATTGGCGTGAATCTGTTCTGACTGATAGAGACAA
+
@DJEJEA?JHJ@8?F?IA3=;8@C95=;=?;>D/:;74792.

Sample Output

1
'''

from Bio import SeqIO
from numpy import average

FILEPATH = r"PHRE_read_quality_distribution\data.txt"

def main():
    with open(FILEPATH) as handle:
        threshold = int(next(handle).strip())
        records = list(SeqIO.parse(handle, "fastq"))
    
    acceptable = sum(1 for r in records if average(r.letter_annotations["phred_quality"]) <= threshold)
    print(acceptable)

if __name__ == "__main__":
    main()