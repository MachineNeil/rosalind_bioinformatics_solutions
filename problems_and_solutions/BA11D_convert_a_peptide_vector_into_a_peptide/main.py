'''
We can also invert the conversion of a peptide into a peptide vector, so that the terms "peptide" and "peptide vector" can be used interchangeably.
Converting Peptide Vector into Peptide Problem

Convert a binary vector into a peptide.

Given: A space-delimited binary vector P.

Return: A peptide whose binary peptide vector matches P. For masses with more than one amino acid, any choice may be used.

Note: In this chapter, all dataset problems implicitly use the standard integer-valued mass table for the regular twenty amino acids. Examples sometimes use imaginary amino acids X and Z having respective integer masses 4 and 5.
Sample Dataset

0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 1 0 0 0 1

Sample Output

XZZXX
'''

FILEPATH = r"BA11D_convert_a_peptide_vector_into_a_peptide\data.txt"

MASS_TABLE = {
    57: "G", 71: "A", 87: "S", 97: "P", 99: "V",
    101: "T", 103: "C", 113: "L", 114: "N", 115: "D",
    128: "K", 129: "E", 131: "M", 137: "H", 147: "F",
    156: "R", 163: "Y", 186: "W"
}

def vector_to_peptide(vector):
    peptide, buffer = "", 0
    for i, v in enumerate(vector):
        if v:
            peptide += MASS_TABLE[i + 1 + buffer]
            buffer = i - 1
    return peptide

def main():
    with open(FILEPATH) as file:
        vector = list(map(int, file.read().strip().split()))
    
    print(vector_to_peptide(vector))

if __name__ == "__main__":
    main()