'''
Implement NumberToPattern

Convert an integer to its corresponding DNA string.

Given: Integers index and k.

Return: NumberToPattern(index, k).
Sample Dataset

45
4

Sample Output

AGTC
'''

FILEPATH = r"BA1M_implement_numbertopattern\data.txt"

def numbertopattern(index, k):
    values = ["A", "C", "G", "T"]
    result = []
    while k > 1:
        result.append(values[index % 4])
        index /= 4
        k -= 1
    return "".join(reversed(result))

def main():
    with open(FILEPATH) as file:
        index = int(file.readline().strip())
        k = int(file.readline().strip())

    pattern = numbertopattern(index, k)

    print(pattern)

if __name__ == "__main__":
    main()