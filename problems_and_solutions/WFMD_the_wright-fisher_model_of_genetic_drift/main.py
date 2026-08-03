'''
Problem

Consider flipping a weighted coin that gives "heads" with some fixed probability p (i.e., p is not necessarily equal to 1/2).

We generalize the notion of binomial random variable from “Independent Segregation of Chromosomes” to quantify the sum of the weighted coin flips. Such a random variable X takes a value of k if a sequence of n independent "weighted coin flips" yields k "heads" and n−k "tails." We write that X∈Bin(n,p).

To quantify the Wright-Fisher Model of genetic drift, consider a population of N diploid individuals, whose 2N chromosomes possess m copies of the dominant allele. As in “Counting Disease Carriers”, set p=m2N. Next, recall that the next generation must contain exactly N individuals. These individuals' 2N alleles are selected independently: a dominant allele is chosen with probability p, and a recessive allele is chosen with probability 1−p.

Given: Positive integers N (N≤7), m (m≤2N), g (g≤6) and k (k≤2N).

Return: The probability that in a population of N diploid individuals initially possessing m copies of a dominant allele, we will observe after g generations at least k copies of a recessive allele. Assume the Wright-Fisher model.
Sample Dataset

4 6 2 1

Sample Output

0.772
'''

from math import factorial

FILEPATH = r"WFMD_the_wright-fisher_model_of_genetic_drift\data.txt"

def p_bin(n, p, k):
    c = factorial(n) // (factorial(k) * factorial(n - k))
    r = (1 - p) ** (n - k)
    return c * r * (p ** k)

def main():
    with open(FILEPATH) as file:
        n, m, g, k = list(map(int, file.read().strip().split()))

    alleles = 2 ** n

    distribution = [0] * (alleles + 1)
    distribution[m] = 1

    for _ in range(g):
        new_distribution = [0] * (alleles + 1)
        for i in range(alleles + 1):
            if distribution[i] == 0:
                continue
            p = i // alleles
            for j in range(alleles + 1):
                new_distribution[j] += distribution[i] * p_bin(alleles, p, j)
        distribution = new_distribution
    resultado = sum(distribution[j + 1] for j in range(alleles - k + 1))

    print(round(resultado, 3))
if __name__ == "__main__":
    main()