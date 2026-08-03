'''
Probability of an Outcome Given a Hidden Path Problem

Given: A string x, followed by the alphabet Σ from which x was constructed, followed by a hidden path π, followed by the states States and emission matrix Emission of an HMM (Σ, States, Transition, Emission).

Return: The conditional probability Pr(x|π) that string x will be emitted by the HMM given the hidden path π.
Sample Dataset

xxyzyxzzxzxyxyyzxxzzxxyyxxyxyzzxxyzyzxzxxyxyyzxxzx
--------
x   y   z
--------
BBBAAABABABBBBBBAAAAAABAAAABABABBBBBABAABABABABBBB
--------
A   B
--------
    x   y   z
A   0.612   0.314   0.074 
B   0.346   0.317   0.336

Sample Output

1.93157070893e-28
'''

from math import log, exp

FILEPATH = r"BA10B_compute_the_probability_of_an_outcome_given_a_hidden_path\data.txt"

def main():
    with open(FILEPATH) as file:
        data = file.read().strip().splitlines()

    string, path = data[0], data[4]
    l1, l2 = (list(map(float, data[9].strip().split("\t")[1:])), list(map(float, data[10].strip().split("\t")[1:])))

    transition_matrix = {
        "Ax": l1[0], "Ay": l1[2], "Az": l1[1],
        "Bx": l2[0], "By": l2[2], "Bz": l2[1]
    }

    probability = 0
    for a, b in zip(path, string):
        probability += log(transition_matrix[a + b])
    
    print(exp(probability))

if __name__ == "__main__":
    main()