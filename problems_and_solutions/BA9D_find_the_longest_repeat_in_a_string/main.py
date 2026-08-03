'''
Although the suffix tree decreases memory requirements from O(|Text|2) to O(|Text|), on average it still requires about 20 times as much memory as Text. In the case of a 3 GB human genome, 60 GB of RAM still presents a memory challenge for most machines. This reveals a dark secret of big-O notation, which is that it ignores constant factors. For long strings such as the human genome, we will need to pay attention to this constant factor, since the expression O(|Text|) applies to both an algorithm with 2 · |Text| memory and an algorithm with 1000 · |Text| memory.

Yet before seeing how we can further reduce the memory needed for multiple pattern matching, we ask you to solve three problems showing how suffix trees can be applied to other pattern matching challenges. The first such problem is the Longest Repeat Problem.
Longest Repeat Problem

Find the longest repeat in a string.

Given: A string Text.

Return: A longest substring of Text that appears in Text more than once. (Multiple solutions may exist, in which case you may return any one.)
Sample Dataset

ATATCGTTTTATCGTT

Sample Output

TATCGTT
'''

from collections import Counter

FILEPATH = r"BA9D_find_the_longest_repeat_in_a_string\data.txt"

def generate_kmers(text, length):
    return Counter(text[i:(i + length)] for i in range(len(text) - length + 1))

def main():
    with open(FILEPATH) as file:
        text = file.read().strip()
    
    for k in range(len(text), 2, -1):
        substrings = generate_kmers(text, k)
        for kmer, count in substrings.items():
            if count > 1:
                print(kmer)
                return

if __name__ == "__main__":
    main()