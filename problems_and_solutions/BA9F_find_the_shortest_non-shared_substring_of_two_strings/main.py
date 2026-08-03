'''
In “Find the Longest Repeat in a String” and “Find the Longest Substring Shared by Two Strings”, we encountered two problems that could be solved using a suffix tree. A third such problem is shown below.
Shortest Non-Shared Substring Problem

Find the shortest substring of one string that does not appear in another string.

Given: Strings Text1 and Text2.

Return: The shortest substring of Text1 that does not appear in Text2. (Multiple solutions may exist, in which case you may return any one.)
Sample Dataset

CCAAGCTGCTAGAGG
CATGCTGGGCTGGCT

Sample Output

AA
'''

FILEPATH = r"BA9F_find_the_shortest_non-shared_substring_of_two_strings\data.txt"

def generate_kmers(text, length):
    return set(text[i:(i + length)] for i in range(len(text) - length + 1))

def main():
    with open(FILEPATH) as file:
        text1, text2 = file.read().strip().splitlines()

    for k in range(len(text1) + 1):
        text1_substrings, text2_substrings = generate_kmers(text1, k), generate_kmers(text2, k)

        for s in text1_substrings:
            if s in text2_substrings:
                print(s)
                return

if __name__ == "__main__":
    main()