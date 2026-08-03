'''
Problem

An online interface to EMBOSS's Needle tool for aligning DNA and RNA strings can be found here.

Use:

    The DNAfull scoring matrix; note that DNAfull uses IUPAC notation for ambiguous nucleotides.
    Gap opening penalty of 10.
    Gap extension penalty of 1.

For our purposes, the "pair" output format will work fine; this format shows the two strings aligned at the bottom of the output file beneath some statistics about the alignment.

Given: Two GenBank IDs.

Return: The maximum global alignment score between the DNA strings associated with these IDs.
Sample Dataset

JX205496.1 JX469991.1

Sample Output

257
'''

from Bio import Entrez, Align
from Bio.Align import substitution_matrices

FILEPATH = r"NEED_pairwise_global_alignment\data.txt"

def main():
    with open(FILEPATH) as file:
        ids = file.read().strip().split()

    Entrez.email = "your_name@your_mail_server.com"
    handle = Entrez.efetch(
        db="nucleotide", 
        id=ids, 
        rettype="gb", 
        retmode="xml"
    )
    records = Entrez.read(handle)
    handle.close()

    seq1 = records[0]["GBSeq_sequence"].upper()
    seq2 = records[1]["GBSeq_sequence"].upper()

    aligner = Align.PairwiseAligner()
    aligner.substitution_matrix = substitution_matrices.load("DNAfull")
    aligner.open_gap_score = -10
    aligner.extend_gap_score = -10
    aligner.mode = "global"

    print(int(aligner.score(seq1, seq2)))

if __name__ == "__main__":
    main()