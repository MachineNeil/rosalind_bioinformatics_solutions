'''
Problem

An array A[1..n] is said to have a majority element if more than half of its entries are the same.

Given: A positive integer k≤20, a positive integer n≤104, and k arrays of size n containing positive integers not exceeding 105.

Return: For each array, output an element of this array occurring strictly more than n/2 times if such element exists, and "-1" otherwise.

Source: Algorithms by Dasgupta, Papadimitriou, Vazirani. McGraw-Hill. 2006.
Sample Dataset

4 8
5 5 5 5 5 5 5 5
8 7 7 7 1 7 3 7
7 1 6 5 10 100 1000 1
5 1 6 7 1 1 10 1

Sample Output

5 7 -1 -1
'''

from collections import Counter

FILEPATH = r"MAJ_majority_element\data.txt"

def main():
    with open(FILEPATH) as file:
        data = file.read().strip().split("\n")
    
    n, _ = map(int, data[0].split())
    arrays = data[1:]

    result = []
    for a in arrays:
        counter = Counter(a.split())
        best = max(counter, key=lambda x: counter[x])
        result.append(best if counter[best] >= (n / 2) else -1)

    print(" ".join(map(str, result)))
    
if __name__ == "__main__":
    main()