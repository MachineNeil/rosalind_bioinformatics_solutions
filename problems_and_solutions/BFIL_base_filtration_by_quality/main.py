'''
Problem

Bad quality bases can be easily trimmed out using certain threshold (defined by quality plot similar to what we did in “Base Quality Distribution”) There is a lot of trimming tools, you can try one of following:

    FASTQ Quality Trimmer tool on the Galaxy. It uses a "sliding window" approach so for a simple trimming of the ends you should set window size 1.

    Trimmomatic. It is a command-line java-based tool, detail description and download link can be found here. For a simple trimming from both ends you should specify parameters LEADING and TRAILING.

Given: FASTQ file, quality cut-off value q, Phred33 quality score assumed.

Return: FASTQ file trimmed from the both ends (removed leading and trailing bases with quality lower than q)
Sample Dataset

20
@Rosalind_0049
GCAGAGACCAGTAGATGTGTTTGCGGACGGTCGGGCTCCATGTGACACAG
+
FD@@;C<AI?4BA:=>C<G=:AE=><A??>764A8B797@A:58:527+,
@Rosalind_0049
AATGGGGGGGGGAGACAAAATACGGCTAAGGCAGGGGTCCTTGATGTCAT
+
1<<65:793967<4:92568-34:.>1;2752)24')*15;1,.3*3+*!
@Rosalind_0049
ACCCCATACGGCGAGCGTCAGCATCTGATATCCTCTTTCAATCCTAGCTA
+
B:EI>JDB5=>DA?E6B@@CA?C;=;@@C:6D:3=@49;@87;::;;?8+

Sample Output

@Rosalind_0049
GCAGAGACCAGTAGATGTGTTTGCGGACGGTCGGGCTCCATGTGACAC
+
FD@@;C<AI?4BA:=>C<G=:AE=><A??>764A8B797@A:58:527
@Rosalind_0049
ATGGGGGGGGGAGACAAAATACGGCTAAGGCAGGGGTCCT
+
<<65:793967<4:92568-34:.>1;2752)24')*15;
@Rosalind_0049
ACCCCATACGGCGAGCGTCAGCATCTGATATCCTCTTTCAATCCTAGCT
+
B:EI>JDB5=>DA?E6B@@CA?C;=;@@C:6D:3=@49;@87;::;;?8
'''

from Bio import SeqIO

FILEPATH_READ  = r"BFIL_base_filtration_by_quality\data.txt"
FILEPATH_WRITE = r"BFIL_base_filtration_by_quality\data_out.txt"

def trim(record, threshold):
    quality = record.letter_annotations["phred_quality"]
    length = len(quality)

    start = next((i for q, i in enumerate(quality) if q >= threshold), length)
    end = next((i for i, q in enumerate(reversed(quality)) if q >= threshold), length)

    return record[start:(length - end if end else length)]

def main():
    with open(FILEPATH_READ) as handle:
        threshold = int(next(handle).strip())
        records = list(SeqIO.parse(handle, "fasta"))

    trimmed = [trim(r, threshold) for r in records]

    with open(FILEPATH_WRITE, "w") as handle:
        SeqIO.write(trimmed, handle, "fastq")

if __name__ == "__main__":
    main()