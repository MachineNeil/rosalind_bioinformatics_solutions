'''
Problem

For a weighted alphabet A and a collection L of positive real numbers, the spectrum graph of L is a digraph constructed in the following way. First, create a node for every real number in L. Then, connect a pair of nodes with a directed edge (u,v) if v>u and v−u is equal to the weight of a single symbol in A. We may then label the edge with this symbol.

In this problem, we say that a weighted string s=s1s2⋯sn matches L if there is some increasing sequence of positive real numbers (w1,w2,…,wn+1) in L such that w(s1)=w2−w1, w(s2)=w3−w2, ..., and w(sn)=wn+1−wn.

Given: A list L (of length at most 100) containing positive real numbers.

Return: The longest protein string that matches the spectrum graph of L (if multiple solutions exist, you may output any one of them). Consult the monoisotopic mass table.
Sample Dataset

3524.8542
3623.5245
3710.9335
3841.974
3929.00603
3970.0326
4026.05879
4057.0646
4083.08025

Sample Output

WMSPG
'''

FILEPATH = r"SGRA_using_the_spectrum_graph_to_infer_peptides\data.txt"

THRESHOLD = 0.0001

MASS_TABLE = {
    "A": 71.03711, "C": 103.00919, "D": 115.02694, "E": 129.04259, "F": 147.06841,
    "G": 57.02146, "H": 137.05891, "I": 113.08406, "K": 128.09496, "L": 113.08406,
    "M": 131.04049, "N": 114.04293, "P": 97.05276, "Q": 128.05858, "R": 156.10111,
    "S": 87.03203, "T": 101.04768, "V": 99.06841, "W": 186.07931, "Y": 163.06333,
}

def find_best_match(mass, threshold=THRESHOLD, table=MASS_TABLE):
    best_aa = None
    best_diff = threshold
    for k, v in table.items():
        current_diff = abs(mass - v)
        if current_diff < best_diff:
            best_aa, best_diff = k, current_diff
    return best_aa

def build_chains(i, values):
    n = len(values)
    chains = [0]
    extended = True

    for j in range(i + 1, n):
        difference = values[j] - values[i]
        best = find_best_match(difference)
        if best:
            extended = True
            for subsequence in build_chains(j, values):
                chains.append(best + subsequence)

    if not extended:
        chains.append([])

    return chains

def find_sequences(values):
    all_chains = []
    for i in range(len(values)):
        for chain in build_chains(i, values):
            if chain:
                all_chains.append(chain)

    return max(all_chains, key=len)

def main():
    with open(FILEPATH) as file:
        values = list(map(float, file.read().strip().splitlines()))

    print("".join(find_sequences(values)))

if __name__ == "__main__":
    main()