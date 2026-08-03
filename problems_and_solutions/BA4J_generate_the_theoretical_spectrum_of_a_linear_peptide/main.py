'''
Given an amino acid string Peptide, we will begin by assuming that it represents a linear peptide. Our approach to generating its theoretical spectrum is based on the assumption that the mass of any subpeptide is equal to the difference between the masses of two prefixes of Peptide. We can compute an array PrefixMass storing the masses of each prefix of Peptide in increasing order, e.g., for Peptide = NQEL, PrefixMass = (0, 114, 242, 371, 484). Then, the mass of the subpeptide of Peptide beginning at position i + 1 and ending at position j can be computed as PrefixMass(j) − PrefixMass(i). For example, when Peptide = NQEL,

Mass(QE) = PrefixMass(3) − PrefixMass(1) = 371 − 114 = 257.

The pseudocode shown on the next step implements this idea. It also represents the alphabet of 20 amino acids and their integer masses as a pair of 20-element arrays AminoAcid and AminoAcidMass, corresponding to the top and bottom rows of the following integer mass table, respectively.

Figure 1

LinearSpectrum(Peptide, AminoAcid, AminoAcidMass)
    PrefixMass(0) ← 0
    for i ← 1 to |Peptide|
        for j ← 1 to 20
            if AminoAcid(j) =  i-th amino acid in Peptide
                PrefixMass(i) ← PrefixMass(i − 1) + AminoAcidMass(j)
    LinearSpectrum ← a list consisting of the single integer 0
    for i ← 0 to |Peptide| − 1
        for j ← i + 1 to |Peptide|
            add PrefixMass(j) − PrefixMass(i) to LinearSpectrum
    return sorted list LinearSpectrum

Linear Spectrum Problem

Generate the ideal linear spectrum of a peptide.

Given: An amino acid string Peptide.

Return: The linear spectrum of Peptide.
Sample Dataset

NQEL

Sample Output

0 113 114 128 129 242 242 257 370 371 484
'''

FILEPATH = r"BA4J_generate_the_theoretical_spectrum_of_a_linear_peptide\data.txt"

MASSES = {
    "G": 57, "A": 71, "S": 87, "P": 97, "V": 99,
    "T": 101, "C": 103, "I": 113, "L": 113, "N": 114,
    "D": 115, "K": 128, "Q": 128, "E": 129, "M": 131,
    "H": 137, "F": 147, "R": 156, "Y": 163, "W": 186,
}

def protein_to_masses(protein):
    l_p = len(protein)
    results = [0]
    for k in range(1, l_p + 1):
        for i in range(l_p - k + 1):
            mass = sum(MASSES[c] for c in protein[i:(i - k - 1)])
            results.append(mass)
    return " ".join(map(str, sorted(results)))

def main():
    with open(FILEPATH) as file:
        protein = file.read().strip()
    
    print(protein_to_masses(protein))

if __name__ == "__main__":
    main()