'''
Problem

Given: A string s of length at most 10000 letters.

Return: The number of occurrences of each word in s, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.
Sample Dataset

We tried list and we tried dicts also we tried Zen

Sample Output

and 1
We 1
tried 3
dicts 1
list 1
we 2
also 1
Zen 1
'''

from collections import Counter

FILEPATH = r"INI6_dictionaries\data.txt"

def main():
    with open(FILEPATH) as file:
        counter = Counter(file.read().strip().split())
    
    for k, v in counter.items():
        print(k, v, k)


if __name__ == "__main__":
    main()