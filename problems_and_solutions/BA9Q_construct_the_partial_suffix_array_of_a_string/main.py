'''
To construct the partial suffix array SuffixArrayk(Text), we first need to construct the full suffix array and then retain only the elements of this array that are divisible by K, along with their indices i.
Partial Suffix Array Construction Problem

Construct the partial suffix array of a string.

Given: A string Text and a positive integer K.

Return: SuffixArrayK(Text), in the form of a list of ordered pairs (i, SuffixArray(i)) for all nonempty entries in the partial suffix array.
Sample Dataset

PANAMABANANAS$
5

Sample Output

1,5
11,10
12,0
'''

FILEPATH_READ = r"BA9Q_construct_the_partial_suffix_array_of_a_string\data.txt"
FILEPATH_WRITE = r"BA9Q_construct_the_partial_suffix_array_of_a_string\data_out.txt"

def main():
    with open(FILEPATH_READ) as file:
        text = next(file).strip()
        k = int(next(file).strip())

    suffix_array = []
    for i in range(len(text)):
        suffix_array.append((i, text[i:]))

    suffix_array = sorted(range(len(text)), key=lambda x: text[x:])

    with open(FILEPATH_WRITE, "w") as file:
        for i, start in enumerate(suffix_array):
            if start % k != 0:
                file.write(f"{i},{start}\n")

if __name__ == "__main__":
    main()