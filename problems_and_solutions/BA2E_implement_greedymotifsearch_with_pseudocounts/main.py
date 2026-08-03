'''
We encountered GreedyMotifSearch in “Implement GreedyMotifSearch”. In this problem, we will power it up with pseudocounts.
Implement GreedyMotifSearch with Pseudocounts

Given: Integers k and t, followed by a collection of strings Dna.

Return: A collection of strings BestMotifs resulting from running GreedyMotifSearch(Dna, k, t) with pseudocounts. If at any step you find more than one Profile-most probable k-mer in a given string, use the one occurring first.
Sample Dataset

3 5
GGCGTTCAGGCA
AAGAATCAGTCA
CAAGGAGTTCGC
CACGTCAATCAC
CAATAATATTCG

Sample Output

TTC
ATC
TTC
ATC
TTC
'''

FILEPATH = r"BA2E_implement_greedymotifsearch_with_pseudocounts\data.txt"

NUCLEOTIDES = "ACGT"

def profile(motifs):
    k = len(motifs[0])
    t = len(motifs)

    profile = {
        "A": [0] * k,
        "C": [0] * k,
        "G": [0] * k,
        "T": [0] * k
    }

    for j in range(k):
        for motif in motifs:
            profile[motif[j]][j] += 1

    for n in NUCLEOTIDES:
        for j in range(k):
            profile[n][j] /= (t * 4)

    return profile

def profile_most_probable_kmer(text, k, profile):
    best_kmer = text[:k]
    best_probability = -1

    for i in range(len(text) - k + 1):
        kmer = text[i:(i + k)]
        probability = 1

        for j in range(k):
            probability *= profile[kmer[j]][j]

        if probability > best_probability:
            best_probability = probability
            best_kmer = kmer

    return best_kmer

def score(motifs):
    k = len(motifs[0])
    t = len(motifs)
    total = 0

    for j in range(k):
        counts = {"A": 0, "C": 0, "G": 0, "T": 0}

        for motif in motifs:
            counts[motif[j]] += 1

        total += t - max(counts.values())

    return total

def greedy_motif_search(dna, k, t):
    best_motifs = [s[:k] for s in dna]

    first_string = dna[0]

    for i in range(len(first_string) - k + 1):
        motifs = [first_string[i:(i + k)]]

        for j in range(1, t):
            prof = profile(motifs)
            motifs.append(profile_most_probable_kmer(dna[j], k, prof))

        if score(motifs) < score(best_motifs):
            best_motifs = motifs

    return best_motifs

def main():
    with open(FILEPATH) as file:
        data = file.read().strip().split("\n")
    
    k, t = map(int, data[0].split())
    dna = data[1:]

    result = greedy_motif_search(dna, k, t)
    
    print("\n".join(m for m in result))
    
if __name__ == "__main__":
    main()