'''
Length of a Longest Path in the Manhattan Tourist Problem

Find the length of a longest path in a rectangular city.

Given: Integers n and m, followed by an n × (m+1) matrix Down and an (n+1) × m matrix Right. The two matrices are separated by the "-" symbol.

Return: The length of a longest path from source (0, 0) to sink (n, m) in the n × m rectangular grid whose edges are defined by the matrices Down and Right.
Sample Dataset

4 4
1 0 2 4 3
4 6 5 2 1
4 4 5 2 1
5 6 8 5 3
-
3 2 4 0
3 2 4 2
0 7 3 3
3 3 0 2
1 3 2 2

Sample Output

34
'''

FILEPATH = r"BA5B_find_the_length_of_a_longest_path_in_a_manhattan-like_grid\data.txt"

def longest_manhattan_path(n, m, down, right):
    s = [([0] * (m + 1)) for _ in range(n + 1)]

    for i in range(1, n + 1):
        s[i][0] = s[i - 1][0] + down[i][0]
    
    for j in range(1, m + 1):
        s[0][j] = s[0][j] + right[0][j - 1]

    for r in range(1, n + 1):
        for c in range(1, m + 1):
            from_top = s[r - 1][c] + down[r - 1][c]
            from_left = s[r][c - 1] + right[r][c - 1]
            s[r][c] = max(from_top, from_left)
    
    return s[n][m]

def main():
    with open(FILEPATH) as file:
        data = file.read().strip().splitlines()
    n, m = list(map(int, data[0].split()))
    down = [list(map(int, r.split())) for r in data[1:(n + 1)]]
    right = [list(map(int, r.split())) for r in data[(n + 2):]]

    print(longest_manhattan_path(n, m, down, right))

if __name__ == "__main__":
    main()