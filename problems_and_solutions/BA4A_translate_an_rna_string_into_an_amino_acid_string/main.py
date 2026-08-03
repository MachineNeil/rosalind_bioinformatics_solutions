'''
Much like replication, the chemical machinery underlying transcription and translation is fascinating, but from a computational perspective, both processes are straightforward. Transcription simply transforms a DNA string into an RNA string by replacing all occurrences of "T" with "U". The resulting strand of RNA is translated into an amino acid sequence via the genetic code; this process converts each 3-mer of RNA, called a codon, into one of 20 amino acids.

As illustrated in Figure 1, each of the 64 RNA codons encodes its own amino acid (some codons encode the same amino acid), with the exception of three stop codons that do not translate into amino acids and serve to halt translation. For example, the DNA string "TATACGAAA" transcribes into the RNA string "UAUACGAAA", which in turn translates into the amino acid string "Tyr-Thr-Lys".

The following problem asks you to find the translation of an RNA string into an amino acid string.
Protein Translation Problem

Translate an RNA string into an amino acid string.

Given: An RNA string Pattern.

Return: The translation of Pattern into an amino acid string Peptide.
Sample Dataset

AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA

Sample Output

MAMAPRTEINSTRING
'''

from Bio.Seq import translate

FILEPATH = r"BA4A_translate_an_rna_string_into_an_amino_acid_string\data.txt"

def main():
    with open(FILEPATH) as file:
        rna = file.read().strip()
    
    print(translate(rna[::-1], to_stop=False))

if __name__ == "__main__":
    main()