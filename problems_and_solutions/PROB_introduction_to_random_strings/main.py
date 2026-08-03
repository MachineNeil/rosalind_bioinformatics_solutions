'''
Problem
Figure 1. The graph of the common logarithm function of x. For a given x-value, the corresponding y-value is the exponent to which we must raise 10 to obtain x. Note that x-values between 0 and 1 get mapped to y-values between -infinity and 0.

An array is a structure containing an ordered collection of objects (numbers, strings, other arrays, etc.). We let A[k] denote the k-th value in array A. You may like to think of an array as simply a matrix having only one row.

A random string is constructed so that the probability of choosing each subsequent symbol is based on a fixed underlying symbol frequency.

GC-content offers us natural symbol frequencies for constructing random DNA strings. If the GC-content is x, then we set the symbol frequencies of C and G equal to x2 and the symbol frequencies of A and T equal to 1−x2. For example, if the GC-content is 40%, then as we construct the string, the next symbol is 'G'/'C' with probability 0.2, and the next symbol is 'A'/'T' with probability 0.3.

In practice, many probabilities wind up being very small. In order to work with small probabilities, we may plug them into a function that "blows them up" for the sake of comparison. Specifically, the common logarithm of x (defined for x>0 and denoted log10(x)) is the exponent to which we must raise 10 to obtain x.

See Figure 1 for a graph of the common logarithm function y=log10(x). In this graph, we can see that the logarithm of x-values between 0 and 1 always winds up mapping to y-values between −∞ and 0: x-values near 0 have logarithms close to −∞, and x-values close to 1 have logarithms close to 0. Thus, we will select the common logarithm as our function to "blow up" small probability values for comparison.

Given: A DNA string s of length at most 100 bp and an array A containing at most 20 numbers between 0 and 1.

Return: An array B having the same length as A in which B[k] represents the common logarithm of the probability that a random string constructed with the GC-content found in A[k] will match s exactly.
Sample Dataset

ACGATACAA
0.129 0.287 0.423 0.476 0.641 0.742 0.783

Sample Output

-5.737 -5.217 -5.263 -5.360 -5.958 -6.628 -7.009
'''

import math

FILEPATH = r"PROB_introduction_to_random_strings\data.txt"

def main():
    with open(FILEPATH) as file:
        dna, gc_contents = file.readlines()
    
    dna = dna.strip()
    gc_contents = map(float, gc_contents.strip().split())
    
    results = []
    for p_gc in gc_contents:
        p_g_or_c = p_gc // 2
        p_a_or_t = (1 - p_gc ) // 2

        log_prob = 0
        for base in dna:
            if base in 'GC':
                log_prob += math.log10(p_g_or_c)
            else:
                log_prob += math.log10(p_a_or_t)
            
        results.append(round(log_prob, 3))

    print(' '.join(f"{r:.3f}" for r in results))
    
if __name__ == "__main__":
    main()