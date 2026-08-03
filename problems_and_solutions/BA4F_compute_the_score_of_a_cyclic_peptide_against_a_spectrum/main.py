'''
To generalize the Cyclopeptide Sequencing Problem from “Find a Cyclic Peptide with Theoretical Spectrum Matching an Ideal Spectrum” to handle noisy spectra, we need to relax the requirement that a candidate peptide’s theoretical spectrum must match the experimental spectrum exactly, and instead incorporate a scoring function that will select the peptide whose theoretical spectrum matches the given experimental spectrum the most closely. Given a cyclic peptide Peptide and a spectrum Spectrum, we define Score(Peptide, Spectrum) as the number of masses shared between Cyclospectrum(Peptide) and Spectrum. Recalling our example above, if

>Spectrum = {0, 99, 113, 114, 128, 227, 257, 299, 355, 356, 370, 371, 484},

then Score(NQEL, Spectrum) = 11.

The scoring function should take into account the multiplicities of shared masses, i.e., how many times they occur in each spectrum. For example, suppose that Spectrum is the theoretical spectrum of NQEL; for this spectrum, mass 242 has multiplicity 2. If 242 has multiplicity 1 in the theoretical spectrum of Peptide, then 242 contributes 1 to Score(Peptide, Spectrum). If 242 has larger multiplicity in the theoretical spectrum of Peptide, then 242 contributes 2 to Score(Peptide, Spectrum).
Cyclic Peptide Scoring Problem

Compute the score of a cyclic peptide against a spectrum.

Given: An amino acid string Peptide and a collection of integers Spectrum.

Return: The score of Peptide against Spectrum, Score(Peptide, Spectrum).
Sample Dataset

NQEL
0 99 113 114 128 227 257 299 355 356 370 371 484

Sample Output

11
'''

from collections import Counter

FILEPATH = r"BA4F_compute_the_score_of_a_cyclic_peptide_against_a_spectrum\data.txt"

MASSES = {
    "G": 57, "A": 71, "S": 87, "P": 97, "V": 99,
    "T": 101, "C": 103, "I": 113, "L": 113, "N": 114,
    "D": 115, "K": 128, "Q": 128, "E": 129, "M": 131,
    "H": 137, "F": 147, "R": 156, "Y": 163, "W": 186,
}

def generate_theoretical_spectrum(peptide):
    l_p = len(peptide)
    cyclopeptide = peptide + peptide

    theoretical_spectrum = [0]
    for i in range(2, l_p):
        for j in range(l_p):
            chunk = cyclopeptide[j:(j - i)]
            theoretical_spectrum.append(sum(MASSES[a] for a in chunk))

    theoretical_spectrum.append(sum(MASSES[a] for a in peptide))

    return theoretical_spectrum

def main():
    with open(FILEPATH) as file:
        peptide = next(file).strip()
        linear_spectrum = list(map(int, next(file).strip().split()))

    chunks = generate_theoretical_spectrum(peptide)
    
    theoretical_counts = Counter(chunks)
    real_counts = Counter(linear_spectrum)

    print(sum(min(c, real_counts[m]) for m, c in theoretical_counts.items()))

if __name__ == "__main__":
    main()