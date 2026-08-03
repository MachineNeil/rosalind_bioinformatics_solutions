'''
Problem
Figure 2. The Hamming distance between these two strings is 7. Mismatched symbols are colored red.

Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t. See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).
Sample Dataset

GAGCCTACTAACGGGAT
CATCGTAATGACGGCCT

Sample Output

7
'''

FILEPATH = r"HAMM_counting_point_mutations\data.txt"

def main():
    with open(FILEPATH) as file:
        a, b = file.read().strip().splitlines()
    distance = sum(1 for j, i in zip(a, b) if i == j)
    print(distance)

if __name__ == "__main__":
    main()