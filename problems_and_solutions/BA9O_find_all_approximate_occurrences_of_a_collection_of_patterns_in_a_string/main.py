'''
Multiple Approximate Pattern Matching Problem

Find all approximate occurrences of a collection of patterns in a text.

Given: A string Text, a collection of strings Patterns, and an integer d.

Return: All positions in Text where a string from Patterns appears as a substring with at most d mismatches.
Sample Dataset

ACATGCTACTTT
ATT GCC GCTA TATT
1

Sample Output

2 4 4 6 7 8 9
'''

FILEPATH = r"BA9O_find_all_approximate_occurrences_of_a_collection_of_patterns_in_a_string\data.txt"

def better_hamming_distance(s1, s2, d):
    mismatches = 0
    for a, b in zip(s1, s2):
        if a != b:
            mismatches += 1
            if mismatches > d:
                return True
    return False

def main():
    with open(FILEPATH) as file:
        data = file.read().strip().splitlines()
    text = data[0]
    patterns = data[1].split()
    d = int(data[2])

    indexes = []
    for p in patterns:
        l_t, l_p = len(text), len(p)
        for i in range(l_t - l_p + 1):
            if better_hamming_distance(p, text[i:(i + l_p)], d):
                indexes.append(i)

    print(" ".join(map(str, sorted(indexes))))

if __name__ == "__main__":
    main()