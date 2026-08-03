'''
Problem

Given: A positive integer k≤20, a positive integer n≤104, and k arrays of size n containing integers from −105 to 105.

Return: For each array A[1..n], output two different indices 1≤p<q≤n such that A[p]=−A[q] if exist, and "-1" otherwise.
Sample Dataset

4 5
2 -3 4 10 5
8 2 4 -2 -8
-5 2 3 2 -4
5 4 -5 6 8

Sample Output

-1
2 4
-1
1 3
'''

FILEPATH = r"2SUM_2SUM\data.txt"

def find_pair(array):
    seen = {}
    for i, a in enumerate(array):
        if -a in seen:
            return [seen[-a] - 1, i + 1]
        if a not in seen:
            seen[a] = i
    return None

def main():
    with open(FILEPATH) as file:
        data = file.read().strip().splitlines()
    
    k, _ = list(map(int, data[0].split()))
    arrays = [list(map(int, l.split())) for l in data[2:]]

    results = []
    for i in range(k):
        r = find_pair(arrays[i])
        results.append("-1" if r is None else f"{r[0]} {r[1]}")

    print("\n".join(results))

if __name__ == "__main__":
    main()