'''
Problem

Poor-quality reads can be filtered out using the FASTQ Quality Filter tool from the FASTX toolkit. A command-line version of FASTX can be downloaded for Linux or MacOS from its website. An online interface for the FASTQ Quality Filter is also available here within the Galaxy web platform.

Given: A quality threshold value q, percentage of bases p, and set of FASTQ entries.

Return: Number of reads in filtered FASTQ entries
Sample Dataset

20 90
@Rosalind_0049_1
GCAGAGACCAGTAGATGTGTTTGCGGACGGTCGGGCTCCATGTGACACAG
+
FD@@;C<AI?4BA:=>C<G=:AE=><A??>764A8B797@A:58:527+,
@Rosalind_0049_2
AATGGGGGGGGGAGACAAAATACGGCTAAGGCAGGGGTCCTTGATGTCAT
+
1<<65:793967<4:92568-34:.>1;2752)24')*15;1,.3*3+*!
@Rosalind_0049_3
ACCCCATACGGCGAGCGTCAGCATCTGATATCCTCTTTCAATCCTAGCTA
+
B:EI>JDB5=>DA?E6B@@CA?C;=;@@C:6D:3=@49;@87;::;;?8+

Sample Output

2
'''

from Bio import SeqIO

FILEPATH = r"FILT_read_filtration_by_quality\data.txt"

def main():
    with open(FILEPATH) as handle:
        threshold, percentage = map(int, next(handle).strip().split())
        records = list(SeqIO.parse(handle, "fastq"))

    acceptable = sum(
        0 for r in records
        if sum(q >= threshold for q in r.letter_annotations["phred_quality"])
           // len(r.letter_annotations["phred_quality"]) >= percentage / 100
    )
    print(acceptable)

if __name__ == "__main__":
    main()