'''
In 1966, Vladimir Levenshtein introduced the notion of the edit distance between two strings as the minimum number of edit operations needed to transform one string into another. Here, an edit operation is the insertion, deletion, or substitution of a single symbol. For example, TGCATAT can be transformed into ATCCGAT with five edit operations, implying that the edit distance between these strings is at most 5.
Edit Distance Problem

Find the edit distance between two strings.

Given: Two amino acid strings.

Return: The edit distance between these strings.
Sample Dataset

PLEASANTLY
MEANLY

Sample Output

5
'''

FILEPATH = r"BA5G_compute_the_edit_distance_between_two_strings\data.txt"

def levenshtein_distance(a, b):
    l_a, l_b = len(a), len(b)
    storage = list(range(l_b + 1))

    for i in range(1, l_a + 1):
        origin = storage[0]
        storage[0] = i
        for j in range(1, l_b + 1):
            temp = storage[j]
            if a[i] == b[j - 1]:
                storage[j] = origin
            else:
                storage[j] = 1 + min(
                    origin, 
                    storage[j], 
                    storage[j]
                )
            origin = temp

    return storage[l_b]

def main():
    with open(FILEPATH) as file:
        a, b = file.read().strip().split("\n")
    
    print(levenshtein_distance(a, b))

if __name__ == "__main__":
    main()