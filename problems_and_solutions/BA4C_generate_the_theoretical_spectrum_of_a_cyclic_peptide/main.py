'''
The workhorse of peptide sequencing is the mass spectrometer, an expensive molecular scale that shatters molecules into pieces and then weighs the resulting fragments. The mass spectrometer measures the mass of a molecule in daltons (Da); 1 Da is approximately equal to the mass of a single nuclear particle (i.e., a proton or neutron).

We will approximate the mass of a molecule by simply adding the number of protons and neutrons found in the molecule’s constituent atoms, which yields the molecule’s integer mass. For example, the amino acid "Gly", which has chemical formula C2H3ON, has an integer mass of 57, since 2·12 + 3·1 + 1·16 + 1·14 = 57. Yet 1 Da is not exactly equal to the mass of a proton/neutron, and we may need to account for different naturally occurring isotopes of each atom when weighing a molecule. As a result, amino acids typically have non-integer masses (e.g., "Gly" has total mass equal to approximately 57.02 Da); for simplicity, however, we will work with the integer mass table given in Figure 1.

The theoretical spectrum of a cyclic peptide Peptide, denoted Cyclospectrum(Peptide), is the collection of all of the masses of its subpeptides, in addition to the mass 0 and the mass of the entire peptide. We will assume that the theoretical spectrum can contain duplicate elements, as is the case for "NQEL" (shown in Figure 2), where "NQ" and "EL" have the same mass.
Generating Theoretical Spectrum Problem

Generate the theoretical spectrum of a cyclic peptide.

Given: An amino acid string Peptide.

Return: Cyclospectrum(Peptide).
Sample Dataset

LEQN

Sample Output

0 113 114 128 129 227 242 242 257 355 356 370 371 484
'''

MASSES = {
    "G": 57, "A": 71, "S": 87, "P": 97, "V": 99,
    "T": 101, "C": 103, "I": 113, "L": 113, "N": 114,
    "D": 115, "K": 128, "Q": 128, "E": 129, "M": 131,
    "H": 137, "F": 147, "R": 156, "Y": 163, "W": 186,
}

FILEPATH = r"BA4C_generate_the_theoretical_spectrum_of_a_cyclic_peptide\data.txt"

def main():
    with open(FILEPATH) as file:
        protein = file.read().strip()

    cyclic = protein + protein[::-1]
    l_p = len(protein)

    subpeptides = ["", protein] + [cyclic[(i + 1):(i + length)] for i in range(l_p) for length in range(1, l_p)]

    masses = [sum(MASSES[a] for a in p) for p in subpeptides]

    print(" ".join(map(str, sorted(masses))))

if __name__ == "__main__":
    main()