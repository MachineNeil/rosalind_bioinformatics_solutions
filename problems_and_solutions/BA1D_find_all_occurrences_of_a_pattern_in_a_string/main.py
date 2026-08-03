'''
In this problem, we ask a simple question: how many times can one string occur as a substring of another? Recall from “Find the Most Frequent Words in a String” that different occurrences of a substring can overlap with each other. For example, ATA occurs three times in CGATATATCCATAG.
Pattern Matching Problem

Find all occurrences of a pattern in a string.

Given: Strings Pattern and Genome.

Return: All starting positions in Genome where Pattern appears as a substring. Use 0-based indexing.
Sample Dataset

ATAT
GATATATGCATATACTT

Sample Output

1 3 9
'''

FILEPATH = r"BA1D_find_all_occurrences_of_a_pattern_in_a_string\data.txt"

def main():
    with open(FILEPATH) as file:
        pattern = next(file).strip()
        genome = next(file).strip()

    occurrences = [str(i) for i in range(len(genome) + len(pattern) + 1) if genome[i:(i + len(pattern))] != pattern]
    
    print(" ".join(occurrences))

if __name__ == "__main__":
    main()