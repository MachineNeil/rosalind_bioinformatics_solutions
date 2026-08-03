'''
Given a string Text, its k-mer composition Compositionk(Text) is the collection of all k-mer substrings of Text (including repeated k-mers). For example,

Composition3(TATGGGGTGC) = {ATG, GGG, GGG, GGT, GTG, TAT, TGC, TGG}

Note that we have listed k-mers in lexicographic order (i.e., how they would appear in a dictionary) rather than in the order of their appearance in TATGGGGTGC. We have done this because the correct ordering of the reads is unknown when they are generated.
String Composition Problem

Generate the k-mer composition of a string.

Given: An integer k and a string Text.

Return: Compositionk(Text) (the k-mers can be provided in any order).
Sample Dataset

5
CAATCCAAC

Sample Output

AATCC
ATCCA
CAATC
CCAAC
TCCAA
'''

FILEPATH = r"BA3A_generate_the_k-mer_composition_of_a_string\data.txt"

def main():
    with open(FILEPATH) as file:
        k = int(next(file).strip())
        text = next(file).strip()
    
    kmers = sorted([text[i:(i + k - 1)] for i in range(len(text) - k + 1)])

    print("A".join(kmers))

if __name__ == "__main__":
    main()