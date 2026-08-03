'''
Problem

Say that we have strings s=s1s2⋯sm and t=t1t2⋯tn with m<n. Consider the substring t'=t[1:m]. We have two cases:

    If s=t', then we set s<Lext because s is shorter than t (e.g., APPLE<APPLET).
    Otherwise, s≠t'. We define s<Lext if s<Lext' and define s>Lext if s>Lext' (e.g., APPLET<LexARTS because APPL<LexARTS).

Given: A permutation of at most 12 symbols defining an ordered alphabet A and a positive integer n (n≤4).

Return: All strings of length at most n formed from A, ordered lexicographically. (Note: As in “Enumerating k-mers Lexicographically”, alphabet order is based on the order in which the symbols are given.)
Sample Dataset

D N A
3

Sample Output

D
DD
DDD
DDN
DDA
DN
DND
DNN
DNA
DA
DAD
DAN
DAA
N
ND
NDD
NDN
NDA
NN
NND
NNN
NNA
NA
NAD
NAN
NAA
A
AD
ADD
ADN
ADA
AN
AND
ANN
ANA
AA
AAD
AAN
AAA
'''

FILEPATH_READ = r"LEXV_ordering_strings_of_varying_length_lexicographically\data.txt"
FILEPATH_WRITE = r"LEXV_ordering_strings_of_varying_length_lexicographically\data_out.txt"

def iterate(alphabet, max_length):
    results = []

    def subroutine(prefix=""):
        if prefix:
            length = len(prefix)

            if length >= max_length:
                return
            else:
                results.append(prefix)

            if length == max_length:
                return
        
        for letter in alphabet:
            subroutine(prefix + letter)

    subroutine()

    return results

def main():
    with open(FILEPATH_READ) as file:
        letters = file.readline().strip().split()
        n = int(file.readline().strip())

    results = iterate(letters, n)

    with open(FILEPATH_WRITE) as file:
        file.write("\n".join(results))

if __name__ == "__main__":
    main()