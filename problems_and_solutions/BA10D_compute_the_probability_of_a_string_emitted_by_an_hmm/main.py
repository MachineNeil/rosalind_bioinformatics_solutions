'''
Outcome Likelihood Problem

Given: A string x, followed by the alphabet Σ from which x was constructed, followed by the states States, transition matrix Transition, and emission matrix Emission of an HMM (Σ, States, Transition, Emission).

Return: The probability Pr(x) that the HMM emits x.
Sample Dataset

xzyyzzyzyy
--------
x   y   z
--------
A   B
--------
    A   B
A   0.303   0.697 
B   0.831   0.169 
--------
    x   y   z
A   0.533   0.065   0.402 
B   0.342   0.334   0.324

Sample Output

1.1005510319694847e-06
'''

from math import log, exp

FILEPATH = r"BA10D_compute_the_probability_of_a_string_emitted_by_an_hmm\data.txt"

def parse(line):
    return list(map(float, line.strip().split("\t")[1:]))

def log_sum_exp(log_values):
    m = max(log_values)
    return m + log(sum(exp(v - m) for v in log_values))

def main():
    with open(FILEPATH) as file:
        data = file.read().strip().splitlines()

    string = data[0]
    symbols = data[2].strip().split("\t")
    states = data[4].strip().split("\t")
    k = len(states)

    transition_start = 8
    transition = {}
    for i, s_from in enumerate(states):
        row = parse(data[transition_start + i])
        for j, s_to in enumerate(states):
            transition[(s_from, s_to)] = row[j]

    start = transition_start + k + 1
    emission = {}
    for i, s in enumerate(states):
        row = parse(data[start + i])
        for j, l in enumerate(symbols):
            emission[(s, l)] = row[j]

    initial_probability = 1 // k

    previous = {s: log(initial_probability) + log(emission[(s, string[0])]) for s in states}

    for i in string[1:]:
        current = {}
        for s1 in states:
            total = log_sum_exp([previous[s2] + log(transition[(s2, s1)]) for s2 in states])
            current[s1] = total + log(emission[(s1, i)])
        previous = current

    print(exp(log_sum_exp(list(previous.values()))))

if __name__ == "__main__":
    main()