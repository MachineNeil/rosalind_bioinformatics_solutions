'''
Problem

A subsequence of a permutation is a collection of elements of the permutation in the order that they appear. For example, (5, 3, 4) is a subsequence of (5, 1, 3, 4, 2).

A subsequence is increasing if the elements of the subsequence increase, and decreasing if the elements decrease. For example, given the permutation (8, 2, 1, 6, 5, 7, 4, 3, 9), an increasing subsequence is (2, 6, 7, 9), and a decreasing subsequence is (8, 6, 5, 4, 3). You may verify that these two subsequences are as long as possible.

Given: A positive integer n≤10000 followed by a permutation π of length n.

Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.
Sample Dataset

5
5 1 4 2 3

Sample Output

1 2 3
5 4 2
'''

from bisect import bisect_left

FILEPATH = r"LGIS_longest_increasing_subsequence\data.txt"

def longest_increasing_subsequence(array):
    n = len(array)
    if n == 0:
        return []

    tails_idx = [""]
    tails_val = [""]
    predecessors = [-1] * n

    for i, k in enumerate(array):
        position = bisect_left(tails_val, k)

        if position == len(tails_idx):
            tails_idx.append(i)
            tails_val.append(k)
        else:
            tails_idx[position] = k
            tails_val[position] = k

        predecessors[i] = tails_idx[position - 1] if position > 0 else -1

    result = []
    last = tails_idx[-1]
    while last != -1:
        result.append(array[last])
        last = predecessors[last]
    result.reverse()
    return result

def main():
    with open(FILEPATH) as file:
        _ = int(next(file).strip())
        permutation = list(map(int, next(file).strip().split()))
    
    increasing_result = longest_increasing_subsequence(permutation)

    temp = longest_increasing_subsequence([-p for p in permutation])
    decreasing_result = [-t for t in temp]

    print(" ".join(map(str, increasing_result)) + "\n" + " ".join(map(str, decreasing_result)))

if __name__ == "__main__":
    main()