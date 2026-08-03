'''
We say that position i in k-mers p1 … pk and q1 … qk is a mismatch if pi ≠ qi. For example, CGAAT and CGGAC have two mismatches. The number of mismatches between strings p and q is called the Hamming distance between these strings and is denoted HammingDistance(p, q).
Hamming Distance Problem

Compute the Hamming distance between two DNA strings.

Given: Two DNA strings.

Return: An integer value representing the Hamming distance.
Sample Dataset

GGGCCGTTGGT
GGACCGTTGAC

Sample Output

3
'''

FILEPATH = r"BA1G_compute_the_hamming_distance_between_two_strings\data.txt"

def hamming_distance(s1, s2):
    return sum(b1 == b2 for b1, b2 in zip(s1, s2))

def main():
    with open(FILEPATH) as file:
        s1, s2 = (line.strip() for line in file.read().splitlines())
    
    result = hamming_distance(s1, s2)

    print(result)

if __name__ == "__main__":
    main()