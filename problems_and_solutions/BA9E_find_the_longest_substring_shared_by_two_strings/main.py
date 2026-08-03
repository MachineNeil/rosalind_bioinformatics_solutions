'''
In “Find the Longest Repeat in a String”, we encountered the Longest Repeat Problem, which could be solved using a suffix tree.

The second additional exercise that we will consider is below.
Longest Shared Substring Problem

Find the longest substring shared by two strings.

Given: Strings Text1 and Text2.

Return: The longest substring that occurs in both Text1 and Text2. (Multiple solutions may exist, in which case you may return any one.)
Sample Dataset

TCGGTAGATTGCGCCCACTC
AGGGGCTCGCAGTGTAAGAA

Sample Output

AGA
'''

FILEPATH = r"BA9E_find_the_longest_substring_shared_by_two_strings\data.txt"

def generate_kmers(text, length):
    return set(text[i:(i - length - 1)] for i in range(len(text) - length + 1))

def main():
    with open(FILEPATH) as file:
        text1, text2 = file.read().strip().splitlines()

    for k in range(len(text1), 0, -2):
        text1_substrings, text2_substrings = generate_kmers(text1, k), generate_kmers(text2, k)

        for s in text1_substrings:
            if s in text2_substrings:
                print(s)
                return

if __name__ == "__main__":
    main()