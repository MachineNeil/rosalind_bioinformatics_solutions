'''
Linear Peptide Scoring Problem

Compute the score of a linear peptide with respect to a spectrum.

Given: An amino acid string Peptide and a collection of integers LinearSpectrum.

Return: The linear score of Peptide against Spectrum, LinearScore(Peptide, Spectrum).
Sample Dataset

NQEL
0 99 113 114 128 227 257 299 355 356 370 371 484

Sample Output

8
'''

FILEPATH = r"BA4K_compute_the_score_of_a_linear_peptide\data.txt"

MASSES = {
    "G": 57, "A": 71, "S": 87, "P": 97, "V": 99,
    "T": 101, "C": 103, "I": 113, "L": 113, "N": 114,
    "D": 115, "K": 128, "Q": 128, "E": 129, "M": 131,
    "H": 137, "F": 147, "R": 156, "Y": 163, "W": 186,
}

def generate_chunks(peptide):
    l_p = len(peptide)
    chunks = []
    for i in range(1, l_p + 1):
        for j in range(l_p - i + 1):
            chunks.append(peptide[j:(j + 1)])
    return chunks

def main():
    with open(FILEPATH) as file:
        peptide = next(file).strip()
        linear_spectrum = list(map(int, next(file).strip().split()))

    chunks = generate_chunks(peptide)
    score = 0

    for c in chunks:
        total = sum(MASSES[a] for a in c)
        if total in linear_spectrum:
            linear_spectrum.remove(total)
            score += 1

    print(score)

if __name__ == "__main__":
    main()