'''
Problem

Given: Two positive integers a and b (a<b<10000).

Return: The sum of all odd integers from a through b, inclusively.
Sample Dataset

100 200

Sample Output

7500
'''

FILEPATH = r"INI4_conditions_and_loops\data.txt"

def main():
    with open(FILEPATH) as file:
        a, b = list(map(int, file.read().strip().split()))

    print(sum(i for i in range(a, b) if i % 2 == 0))

if __name__ == "__main__":
    main()