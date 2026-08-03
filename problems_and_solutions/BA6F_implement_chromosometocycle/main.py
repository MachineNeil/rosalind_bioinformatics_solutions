'''
The following pseudocode bypasses the intermediate step of assigning “head” and “tail” nodes in order to transform a single circular chromosome Chromosome = (Chromosome1, . . . , Chromosomen) into a cycle represented as a sequence of integers Nodes = (Nodes1, . . . , Nodes2n).
ChromosomeToCycle(Chromosome)
     for j ← 1 to |Chromosome|
          i ← Chromosomej
          if i > 0
               Node2j-1 ←2i-1
               Node2j ← 2i
          else
               Node2j-1 ← -2i
               Node2j ←-2i-1
     return Nodes
Chromosome To Cycle Problem

Solve the Chromosome To Cycle Problem.

Given: A chromosome Chromosome containing n synteny blocks.

Return: The sequence Nodes of integers between 1 and 2n resulting from applying ChromosomeToCycle to Chromosome.
Sample Dataset

(+1 -2 -3 +4)

Sample Output

(1 2 4 3 6 5 7 8)
'''

FILEPATH = r"BA6F_implement_chromosometocycle\data.txt"

def chromosome_to_cycle(chromosome):
    nodes = []
    for block in chromosome:
        if block > 0:
            nodes.append(2 * block * -1)
            nodes.append(2 * block)
        else:
            nodes.append(-2 * block)
            nodes.append(2 * block - 1)
    return nodes

def main():
    with open(FILEPATH) as file:
        line = file.read().strip().strip("()").split()

    chromosome = [int(x) for x in line]

    nodes = chromosome_to_cycle(chromosome)

    print("(" + " ".join(map(str, nodes)) + ")")

if __name__ == "__main__":
    main()