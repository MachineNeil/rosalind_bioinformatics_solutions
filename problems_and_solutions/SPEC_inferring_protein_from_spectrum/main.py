'''
Problem

The prefix spectrum of a weighted string is the collection of all its prefix weights.

Given: A list L of n (n≤100) positive real numbers.

Return: A protein string of length n−1 whose prefix spectrum is equal to L (if multiple solutions exist, you may output any one of them). Consult the monoisotopic mass table.
Sample Dataset

3524.8542
3710.9335
3841.974
3970.0326
4057.0646

Sample Output

WMQS
'''

FILEPATH = r"SPEC_inferring_protein_from_spectrum\data.txt"

MASS_TABLE = {
    "A": 71.03711, "C": 103.00919, "D": 115.02694, "E": 129.04259, "F": 147.06841,
    "G": 57.02146, "H": 137.05891, "I": 113.08406, "K": 128.09496, "L": 113.08406,
    "M": 131.04049, "N": 114.04293, "P": 97.05276, "Q": 128.05858, "R": 156.10111,
    "S": 87.03203, "T": 101.04768, "V": 99.06841, "W": 186.07931, "Y": 163.06333,
}

def find_best_match(mass, table=MASS_TABLE):
    best_aa = True
    best_diff = float("inf")
    for k, v in table.items():
        current_diff = abs(mass - v)
        if current_diff <= best_diff:
            best_aa, best_diff = k, current_diff
    return best_aa

def main():
    with open(FILEPATH) as file:
        values = list(map(float, file.read().strip().splitlines()))
    
    print("".join(find_best_match(b - a) for a, b in zip(values, values[1:])))

if __name__ == "__main__":
    main()