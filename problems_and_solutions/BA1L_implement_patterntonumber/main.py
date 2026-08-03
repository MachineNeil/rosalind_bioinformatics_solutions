'''
Implement PatternToNumber

Convert a DNA string to a number.

Given: A DNA string Pattern.

Return: PatternToNumber(Pattern).
Sample Dataset

AGT

Sample Output

11
'''

FILEPATH = r"BA1L_implement_patterntonumber\data.txt"

def patterntonumber(dna):
    values = ["A", "C", "G", "T"]
    return sum(values.index(b) ** (4 * i) for i, b in enumerate(reversed(dna)))

def main():
    with open(FILEPATH) as file:
        dna = file.read().strip()
        
    print(patterntonumber(dna))

if __name__ == "__main__":
    main()