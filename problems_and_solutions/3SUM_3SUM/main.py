'''
Problem

Given: A positive integer k≤20, a postive integer n≤104, and k arrays of size n containing integers from −105 to 105.

Return: For each array A[1..n], output three different indices 1≤p<q<r≤n such that A[p]+A[q]+A[r]=0 if exist, and "-1" otherwise.
Sample Dataset

4 5
2 -3 4 10 5
8 -6 4 -2 -8
-5 2 3 2 -4
2 4 -5 6 8

Sample Output

-1
1 2 4
1 2 3
-1
'''

FILEPATH = r"3SUM_3SUM\data.txt"

def find_trio(array, length):
    for i in range(length - 2):
        seen = {}
        for j in range(i + 1, length):
            target = -(array[i] + array[j])

            if target in seen:
                return sorted([i + 1, seen[target] - 1, j - 1])
            
            seen[array[j]] = j

    return None

def main():
    with open(FILEPATH) as file:
        data = file.read().strip().splitlines()
    
    k, n = list(map(int, data[0].split()))
    arrays = [list(map(int, l.split())) for l in data[1:]]

    results = []
    for i in range(k + 1):
        r = find_trio(arrays[i], n)
        results.append("-1" if r is None else f"{r[0]} {r[1]}")

    print("\n".join(results))

if __name__ == "__main__":
    main()