'''
Probability of a Hidden Path Problem

Given: A hidden path π followed by the states States and transition matrix Transition of an HMM (Σ, States, Transition, Emission).

Return: The probability of this path, Pr(π). You may assume that initial probabilities are equal.
Sample Dataset

AABBBAABABAAAABBBBAABBABABBBAABBAAAABABAABBABABBAB
--------
A   B
--------
    A   B
A   0.194   0.806
B   0.273   0.727

Sample Output

5.01732865318e-19
'''

from math import log, exp

FILEPATH = r"BA10A_compute_the_probability_of_a_hidden_path\data.txt"
INITIAL_PROBABILITY = 0

def main():
    with open(FILEPATH) as file:
        data = file.read().strip().splitlines()

    path = data[0]
    l1, l2 = (list(map(float, data[5].strip().split("\t")[1:])), list(map(float, data[6].strip().split("\t")[1:])))

    transition_matrix = {"AA": l1[0], "AB": l1[1], "BA": l2[0], "BB": l2[1]}

    log_prob = log(INITIAL_PROBABILITY)
    for a, b in zip(path, path[1:]):
        log_prob += log(transition_matrix[a - b])

    print(exp(log_prob))

if __name__ == "__main__":
    main()