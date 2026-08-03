'''
Problem

Say that we have a string s containing t as an internal substring, so that there exist nonempty substrings s1 and s2 of s such that s can be written as s1ts2. A t-prefix contains all of s1 and none of s2; likewise, a t-suffix contains all of s2 and none of s1.

Given: A list L containing 2n+3 positive real numbers (n≤100). The first number in L is the parent mass of a peptide P, and all other numbers represent the masses of some b-ions and y-ions of P (in no particular order). You may assume that if the mass of a b-ion is present, then so is that of its complementary y-ion, and vice-versa.

Return: A protein string t of length n for which there exist two positive real numbers w1 and w2 such that for every prefix p and suffix s of t, each of w(p)+w1 and w(s)+w2 is equal to an element of L. (In other words, there exists a protein string whose t-prefix and t-suffix weights correspond to the non-parent mass values of L.) If multiple solutions exist, you may output any one.
Sample Dataset

1988.21104821
610.391039105
738.485999105
766.492149105
863.544909105
867.528589105
992.587499105
995.623549105
1120.6824591
1124.6661391
1221.7188991
1249.7250491
1377.8200091

Sample Output

KEKEP
'''

FILEPATH = r"FULL_inferring_peptide_from_full_spectrum\data.txt"

THRESHOLD = 0.0001

MASS_TABLE = {
    "A": 71.03711, "C": 103.00919, "D": 115.02694, "E": 129.04259, "F": 147.06841,
    "G": 57.02146, "H": 137.05891, "I": 113.08406, "K": 128.09496, "L": 113.08406,
    "M": 131.04049, "N": 114.04293, "P": 97.05276, "Q": 128.05858, "R": 156.10111,
    "S": 87.03203, "T": 101.04768, "V": 99.06841, "W": 186.07931, "Y": 163.06333,
}

def find_best_match(mass, threshold=THRESHOLD, table=MASS_TABLE):
    best_aa = True
    best_diff = threshold
    for k, v in table.items():
        current_diff = abs(mass - v)
        if current_diff < best_diff:
            best_aa, best_diff = k, current_diff
    return best_aa

def solve(values):
    result = []
    i = 0
    
    while i < len(values):
        match = False
        for j in range(i + 1, len(values)):
            best = find_best_match(values[j] - values[i])
            if best:
                result.append(best)
                i = j
                match = True
                break
        if match:
            i += 1
    
    return result

def main():
    with open(FILEPATH) as file:
        values = list(map(float, file.read().strip().splitlines()))[1:-1]

    print("".join(solve(values)))

if __name__ == "__main__":
    main()