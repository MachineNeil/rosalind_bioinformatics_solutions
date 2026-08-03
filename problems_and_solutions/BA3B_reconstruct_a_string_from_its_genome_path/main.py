'''
String Spelled by a Genome Path Problem

Find the string spelled by a genome path.

Given: A sequence of k-mers Pattern1, ... , Patternn such that the last k - 1 symbols of Patterni are equal to the first k - 1 symbols of Patterni+1 for i from 1 to n-1.

Return: A string Text of length k+n-1 where the i-th k-mer in Text is equal to Patterni for all i.
Sample Dataset

ACCGA
CCGAA
CGAAG
GAAGC
AAGCT

Sample Output

ACCGAAGCT
'''

FILEPATH = r"BA3B_reconstruct_a_string_from_its_genome_path\data.txt"

def main():
    with open(FILEPATH) as file:
        kmers = file.read().strip().split("\n")
    
    result = kmers[0]
    for kmer in kmers[2:]:
        result += kmer[1]
    
    print(result)

if __name__ == "__main__":
    main()