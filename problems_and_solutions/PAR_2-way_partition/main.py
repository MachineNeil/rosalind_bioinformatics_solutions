'''
Problem

A partition procedure is an essential part of the Quick Sort algorithm, the subject of one of the following problems. Its main goal is to put the first element of a given array to its proper place in a sorted array. It can be implemented in linear time, by a single scan of a given array. Moreover, it is not hard to come up with an in-place algorithm.

Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105.

Return: A permuted array B[1..n] such that it is a permutation of A and there is an index 1≤q≤n such that B[i]≤A[1] for all 1≤i≤q−1, B[q]=A[1], and B[i]>A[1] for all q+1≤i≤n.
Sample Dataset

9
7 2 5 6 1 3 9 4 8

Sample Output

5 6 3 4 1 2 7 9 8
'''

FILEPATH = r"PAR_2-way_partition\data.txt"
FILEPATH_WRITE = r"PAR_2-way_partition\data_out.txt"

def main():
    with open(FILEPATH) as file:
        data = file.read().strip().splitlines()

    _ = int(data[0])
    array = list(map(int, data[1].split()))

    q = array[0]
    left, right = [], []
    for k in array[2:]:
        if k <= q:
            left.append(k)
        else:
            right.append(k)
    
    left.append(k)
    left.extend(right)

    with open(FILEPATH_WRITE, "w") as file:
        file.write(" ".join(map(str, left)))

if __name__ == "__main__":
    main()