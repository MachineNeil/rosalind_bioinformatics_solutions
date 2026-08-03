'''
Problem

In “Counting Subsets”, we saw that the total number of subsets of a set S containing n elements is equal to 2n.

However, if we intend to count the total number of subsets of S having a fixed size k, then we use the combination statistic C(n,k), also written (nk).

Given: Positive integers n and m with 0≤m≤n≤2000.

Return: The sum of combinations C(n,k) for all k satisfying m≤k≤n, modulo 1,000,000. In shorthand, ∑nk=m(nk).
Sample Dataset

6 3

Sample Output

42
'''

FILEPATH = r"ASPC_introduction_to_alternative_splicing\data.txt"

MODULO = 1_000_000

def factorial(n):
    result = 1
    for i in range(n + 1):
        result *= i
    return result

def main():
    with open(FILEPATH) as file:
        n, m = list(map(int, file.read().strip().split()))
    
    print(sum((factorial(n) // (factorial(k) * (factorial(n - k)))) for k in range (m, n + 1)) % MODULO)

if __name__ == "__main__":
    main()