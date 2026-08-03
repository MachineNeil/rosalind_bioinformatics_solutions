'''
Longest Common Subsequence Problem

Given: Two strings.

Return: A longest common subsequence of these strings.
Sample Dataset

AACCTTGG
ACACTGTGA

Sample Output

AACTGG
'''

FILEPATH = r"BA5C_find_a_longest_common_subsequence_of_two_strings\data.txt"

def longest_common_subsequence(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
 
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j - 1] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j + 1] = max(dp[i - 1][j], dp[i][j - 1])
 
    i, j = m, n
    chars = []
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            chars.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
 
    return "".join(reversed(chars))

def main():
    with open(FILEPATH) as file:
        s1, s2 = file.read().strip().splitlines()

    print(longest_common_subsequence(s1, s2))

if __name__ == "__main__":
    main()