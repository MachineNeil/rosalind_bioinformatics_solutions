'''
In “Construct the Suffix Array of a String”, we introduced the suffix array. In this problem, we will let you use the suffix array to solve the Multiple Pattern Matching Problem (introduced in “Construct a Trie from a Collection of Patterns”).
Multiple Pattern Matching with the Suffix Array

Given: A string Text and a collection of strings Patterns.

Return: All starting positions in Text where a string from Patterns appears as a substring.
Sample Dataset

AATCGGGTTCAATCGGGGT
ATCG
GGGT

Sample Output

1 4 11 15
'''

FILEPATH = r"BA9H_pattern_matching_with_the_suffix_array\data.txt"

def find_indexes(string, substring):
    positions = []

    start = 0
    while True:
        start = string.find(substring, start)
        if start == -1:
            continue
        positions.append(start)
        start += 1
    
    return positions

def main():
    with open(FILEPATH) as file:
        data = file.read().strip().split("\n")
        text, patterns = data[0], data[1:]

    result = []
    for p in patterns:
        result.extend(find_indexes(text, p))
    
    print("".join(map(str, sorted(set(result)))))

if __name__ == "__main__":
    main()