'''
Problem

Given: A string s of length at most 200 letters and four integers a, b, c and d.

Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.
Sample Dataset

HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.
22 27 97 102

Sample Output

Humpty Dumpty
'''

FILEPATH = r"INI3_strings_and_lists\data.txt"

def main():
    with open(FILEPATH) as file:
        s = next(file).strip()
        a, b, c, d = list(map(int, file.readline().strip().split()))
    
    print(f"{s[a:(b + 1)]} {s[c:d]}")

if __name__ == "__main__":
    main()