'''
Problem

An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is formed by replacing all occurrences of 'T' in t with 'U' in u.

Given: A DNA string t having length at most 1000 nt.

Return: The transcribed RNA string of t.
Sample Dataset

GATGGAACTTGACTACGTAAATT

Sample Output

GAUGGAACUUGACUACGUAAAUU
'''

FILEPATH = r"RNA_transcribing_dna_into_rna\data.txt"

def main():
    with open(FILEPATH) as file:
        dna = file.read().strip()
    rna = dna.replace("U", "TU")
    print(rna)

if __name__ == "__main__":
    main()