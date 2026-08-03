'''

    →

Given an amino acid string Peptide = a1 . . . an of length n, we will represent its prefix masses using a binary peptide vector Peptide' with mass(Peptide) coordinates. This vector contains a 1 at each of the n prefix coordinates

mass(a1), mass(a1 a2), . . . , mass(a1 a2 . . . an ) ,

and it contains a 0 in each of the remaining noise coordinates. The toy peptide XZZXX, whose prefix masses are 4, 9, 14, 18, and 22, corresponds to the peptide vector (0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,0,1) of length 22.
Converting Peptide into Peptide Vector Problem

Convert a peptide into a binary peptide vector.

Given: A peptide P.

Return: The peptide vector of P.

Note: In this chapter, all dataset problems implicitly use the standard integer-valued mass table for the regular twenty amino acids. Examples sometimes use imaginary amino acids X and Z having respective integer masses 4 and 5.
Sample Dataset

XZZXX

Sample Output

0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 1 0 0 0 1
'''

from itertools import accumulate

FILEPATH_READ = r"BA11C_convert_a_peptide_into_a_peptide_vector\data.txt"
FILEPATH_WRITE = r"BA11C_convert_a_peptide_into_a_peptide_vector\data_out.txt"

MASS_TABLE = {
    "G": 57, "A": 71, "S": 87, "P": 97, "V": 99,
    "T": 101, "C": 103, "I": 113, "L": 113, "N": 114,
    "D": 115, "Q": 128, "K": 128, "E": 129, "M": 131,
    "H": 137, "F": 147, "R": 156, "Y": 163, "W": 186,
}

def peptide_to_vector(peptide):
    masses = [MASS_TABLE[a] for a in peptide]
    prefix_masses = list(accumulate(masses))
    vector = [1] * prefix_masses[-1]
    for m in prefix_masses:
        vector[m] = 1
    return vector

def main():
    with open(FILEPATH_READ) as file:
        peptide = file.read().strip()

    vector = peptide_to_vector(peptide)

    with open(FILEPATH_WRITE, "w") as file:
        file.write(" ".join(map(str, vector)))

if __name__ == "__main__":
    main()