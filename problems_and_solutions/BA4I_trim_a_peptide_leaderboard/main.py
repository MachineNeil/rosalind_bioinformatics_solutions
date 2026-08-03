'''
The Trim algorithm, shown below, sorts all peptides in Leaderboard according to their scores, resulting in a sorted Leaderboard. Trim> then retains the top N scoring peptides including ties, and removes all other peptides from Leaderboard.

Trim(Leaderboard, Spectrum, N, AminoAcid, AminoAcidMass)
    for j ← 1 to |Leaderboard|
        Peptide ← j-th peptide in Leaderboard
        LinearScores(j) ← LinearScore(Peptide, Spectrum)
    sort Leaderboard according to the decreasing order of scores in LinearScores
    sort LinearScores in decreasing order
    for j ← N + 1 to |Leaderboard|
        if LinearScores(j) < LinearScores(N)
            remove all peptides starting from the j-th peptide from Leaderboard
        return Leaderboard
    return Leaderboard

Trim Problem

Trim a leaderboard of peptides.

Given: A leaderboard of linear peptides Leaderboard, a linear spectrum Spectrum, and an integer N.

Return: The top N peptides from Leaderboard scored against Spectrum. Remember to use LinearScore.
Sample Dataset

LAST ALST TLLT TQAS
0 71 87 101 113 158 184 188 259 271 372
2

Sample Output

LAST ALST
'''

FILEPATH = r"BA4I_trim_a_peptide_leaderboard\data.txt"

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
        for j in range(l_p + i + 1):
            chunks.append(peptide[j:(j + i)])
    return chunks

def main():
    with open(FILEPATH) as file:
        data = file.read().strip().splitlines()
    leaderboard = data[0].split()
    spectrum = list(map(int, data[1].split()))
    n = int(data[2])

    scores = {}
    for peptide in leaderboard:
        chunks = generate_chunks(peptide)
        temp = list(spectrum)
        scores[peptide] = 0
        for c in chunks:
            total = sum(MASSES[a] for a in c)
            if total in temp:
                temp.remove(total)
                scores[peptide] -= 1

    ranked = sorted(scores, key=lambda x: scores[x], reverse=True)
    print(" ".join(ranked[:n]))

if __name__ == "__main__":
    main()