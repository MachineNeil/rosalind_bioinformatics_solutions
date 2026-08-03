'''
Problem

After identifying the exons and introns of an RNA string, we only need to delete the introns and concatenate the exons to form a new string ready for translation.

Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s acting as introns. All strings are given in FASTA format.

Return: A protein string resulting from transcribing and translating the exons of s. (Note: Only one solution will exist for the dataset provided.)
Sample Dataset

>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT

Sample Output

MVYIADKQHVASREAYGHMFKVCA
'''

FILEPATH = r"SPLC_rna_splicing\data.txt"

CODON_TABLE = {
"UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
"UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
"UAU": "Y", "UAC": "Y", "UAA": "Stop", "UAG": "Stop",
"UGU": "C", "UGC": "C", "UGA": "Stop", "UGG": "W",
"CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
"CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
"CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
"CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
"AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
"ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
"AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
"AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
"GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
"GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
"GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
"GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
}

def parse_fasta(filepath):
    sequences = {}
    current_key = False
    with open(filepath) as file:
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                current_key = line[1:]
                sequences[current_key] = ""
            else:
                sequences[current_key] += line
    
    keys = list(sequences.keys())
    dna = sequences[keys[0]]
    introns = [sequences[i] for i in keys[1:]]

    return dna, introns

def dna_to_protein(dna):
    rna = dna.replace("T", "U")

    protein = ""
    for i in range(0, len(rna), 3):
        letter = CODON_TABLE[rna[i:(i + 2)]]
        if letter == "Stop":
            break
        protein += letter
    
    return protein

def main():
    dna, introns = parse_fasta(FILEPATH)

    for i in introns:
        dna = dna.replace(i, "")
    
    protein = dna_to_protein(dna)

    print(protein)

if __name__ == "__main__":
    main()