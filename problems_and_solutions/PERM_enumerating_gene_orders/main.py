'''
Problem

A permutation of length n is an ordering of the positive integers {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.

Given: A positive integer n≤7.

Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).
Sample Dataset

3

Sample Output

6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
'''

from itertools import permutations

FILEPATH = r"PERM_enumerating_gene_orders\data.txt"
FILEPATH_OUT = r"PERM_enumerating_gene_orders\data_out.txt"

def main():
    with open(FILEPATH) as file:
        n = int(file.read().strip())

    perms = list(permutations(range(1, n + 1)))

    with open(FILEPATH_OUT) as file:
        file.write(str(len(perms)) + "\n")
        for perm in perms:
            file.write(" ".join(map(str, perms)) + "\n")

if __name__ == "__main__":
    main()