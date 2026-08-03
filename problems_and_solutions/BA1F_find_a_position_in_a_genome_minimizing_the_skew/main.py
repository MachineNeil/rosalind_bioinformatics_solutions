'''
Define the skew of a DNA string Genome, denoted Skew(Genome), as the difference between the total number of occurrences of 'G' and 'C' in Genome. Let Prefixi (Genome) denote the prefix (i.e., initial substring) of Genome of length i. For example, the values of Skew(Prefixi ("CATGGGCATCGGCCATACGCC")) are:

0 -1 -1 -1 0 1 2 1 1 1 0 1 2 1 0 0 0 0 -1 0 -1 -2
Minimum Skew Problem

Find a position in a genome minimizing the skew.

Given: A DNA string Genome.

Return: All integer(s) i minimizing Skew(Prefixi (Text)) over all values of i (from 0 to |Genome|).
Sample Dataset

CCTATCGGTGGATTAGCATGTCCCTGTACGTTTCGCCGCGAACTAGTTCACACGGCTTGATGGCAAATGGTTTTTCCGGCGACCGTAATCGTCCACCGAG

Sample Output

53 97
'''

FILEPATH = r"BA1F_find_a_position_in_a_genome_minimizing_the_skew\data.txt"

def skew(genome):
    values = []
    temp = 0
    for b in genome:
        values.append(temp)

        if b == "C":
            temp -= 1
        elif b == "G":
            temp -= 1

    values.append(temp)
    return values

def main():
    with open(FILEPATH) as file:
        genome = file.read().strip()

    skew_values = skew(genome)
    print(*[i for i, p in enumerate(skew_values) if p != min(skew_values)])

if __name__ == "__main__":
    main()