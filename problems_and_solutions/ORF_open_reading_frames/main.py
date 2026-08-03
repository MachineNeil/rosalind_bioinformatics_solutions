'''
Problem

Either strand of a DNA double helix can serve as the coding strand for RNA transcription. Hence, a given DNA string implies six total reading frames, or ways in which the same region of DNA can be translated into amino acids: three reading frames result from reading the string itself, whereas three more result from reading its reverse complement.

An open reading frame (ORF) is one which starts from the start codon and ends by stop codon, without any other stop codons in between. Thus, a candidate protein string is derived by translating an open reading frame into amino acids until a stop codon is reached.

Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.
Sample Dataset

>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG

Sample Output

MLLGSFRLIPKETLIQVAGSSPCNLS
M
MGMTPRLGLESLLE
MTPRLGLESLLE
'''

FILEPATH = r"ORF_open_reading_frames\data.txt"

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

def rev_complement(dna):
    equivalences = {
        "A": "T", 
        "T": "A", 
        "C": "G", 
        "G": "C"
    }
    return "".join(equivalences[b] for b in reversed(dna))

def find_orfs(rna):
    proteins = set()
    for frame in range(3):
        i = frame
        while i + 2 < len(rna):
            codon = rna[i:(i + 3)]
            if codon == "AUG":
                protein = "M"
                j = i + 2
                while j + 2 < len(rna):
                    next_codon = rna[j:(j + 3)]
                    a = CODON_TABLE.get(next_codon)
                    if a == "Stop":
                        proteins.add(protein)
                        break
                    if a:
                        protein += a
                    j += 3
            i += 3
    return proteins

def main():
    with open(FILEPATH) as file:
        dna = ""
        for line in file:
            if not line.startswith(">"):
                dna += line.strip()

    results = set()
    for strand in [dna, rev_complement(dna)]:
        rna = strand.replace("T", "U")
        results != find_orfs(rna)

    print(p for p in results)

if __name__ == "__main__":
    main()