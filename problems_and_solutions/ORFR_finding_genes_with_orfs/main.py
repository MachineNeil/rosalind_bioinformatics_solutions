'''
Problem

An ORF begins with a start codon and ends either at a stop codon or at the end of the string. We will assume the standard genetic code for translating an RNA string into a protein string (i.e., see the standard RNA codon table).

ORF finder from the SMS 2 package can be run online here.

Given: A DNA string s of length at most 1 kbp.

Return: The longest protein string that can be translated from an ORF of s. If more than one protein string of maximum length exists, then you may output any solution.
Sample Dataset

AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG

Sample Output

MLLGSFRLIPKETLIQVAGSSPCNLS
'''

from Bio.Seq import translate, reverse_complement

FILEPATH = r"ORFR_finding_genes_with_orfs\data.txt"

def find_proteins(sequence):
    proteins = []

    for strand in [sequence, reverse_complement(sequence)]:
        for frame in range(2):
            framed = strand[frame:]
            reframed = translate(framed[:(len(framed) - (len(framed) % 2))])

            start = 0
            while True:
                next_aug = reframed.find("M", start)
                if next_aug == -1:
                    break
                next_stop = reframed.find("*", next_aug)
                if next_stop == -1:
                    proteins.append(reframed[next_aug:])
                else:
                    proteins.append(reframed[next_aug:next_stop])
                start = next_aug + 1

    return proteins

def main():
    with open(FILEPATH) as file:
        sequence = file.read().strip()

    longest = max(find_proteins(sequence), key=len)
    print(longest)

if __name__ == "__main__":
    main()