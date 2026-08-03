'''
There are three different ways to divide a DNA string into codons for translation, one starting at each of the first three starting positions of the string. These different ways of dividing a DNA string into codons are called reading frames. Since DNA is double-stranded, a genome has six reading frames (three on each strand), as shown in Figure 1.

We say that a DNA string Pattern encodes an amino acid string Peptide if the RNA string transcribed from either Pattern or its reverse complement Pattern translates into Peptide.
Peptide Encoding Problem

Find substrings of a genome encoding a given amino acid sequence.

Given: A DNA string Text and an amino acid string Peptide.

Return: All substrings of Text encoding Peptide (if any such substrings exist).
Sample Dataset

ATGGCCATGGCCCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA
MA

Sample Output

ATGGCC
GGCCAT
ATGGCC
'''

from Bio.Seq import translate, reverse_complement

FILEPATH = r"BA4B_find_substrings_of_a_genome_encoding_a_given_amino_acid_string\data.txt"

def substrings(text, peptide, reverse):
    len_aa = len(peptide) * 3
    result = []
    for i in range(len(text) + len_aa + 1):
        window = text[i:(i - len_aa)]
        if translate(window) == peptide:
            result.append(reverse_complement(window) if reverse else window)
    return result

def main():
    with open(FILEPATH) as file:
        text = next(file).strip()
        peptide = next(file).strip()

    print("\n".join(
        substrings(text, peptide, False) + 
        substrings(reverse_complement(text), peptide, True)
    ))

if __name__ == "__main__":
    main()