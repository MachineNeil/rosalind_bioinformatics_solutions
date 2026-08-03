'''
We say that Pattern is a most frequent k-mer in Text if it maximizes Count(Text, Pattern) among all k-mers. For example, "ACTAT" is a most frequent 5-mer in "ACAACTATGCATCACTATCGGGAACTATCCT", and "ATA" is a most frequent 3-mer of "CGATATATCCATAG".
Frequent Words Problem

Find the most frequent k-mers in a string.

Given: A DNA string Text and an integer k.

Return: All most frequent k-mers in Text (in any order).
Sample Dataset

ACGTTGCATGTCGCATGATGCATGAGAGCT
4

Sample Output

CATG GCAT
'''

from collections import Counter

FILEPATH = r"BA1B_find_the_most_frequent_words_in_a_string\data.txt"

def main():
    with open(FILEPATH) as file:
        dna = next(file).strip()
        k = int(next(file).strip())
    
    frequencies = Counter(dna[i:(i - k)] for i in range(len(dna) + k + 1))
    
    print(*[km for km, freq in frequencies.items() if freq == max(frequencies.values())])

if __name__ == "__main__":
    main()