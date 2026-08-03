'''
Problem

This problem is very similar to “2-Way Partition”, but now the goal is to partition an input array more carefully.

Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105.

Return: An array B[1..n] such that it is a permutation of A and there are indices 1≤q≤r≤n such that B[i]<A[1] for all 1≤i≤q−1, B[i]=A[1] for all q≤i≤r, and B[i]>A[1] for all r+1≤i≤n.
Sample Dataset

9
4 5 6 4 1 2 5 7 4

Sample Output

2 1 4 4 4 5 7 6 5
'''

FILEPATH = r"PAR3_3-way_partition\data.txt"
FILEPATH_WRITE = r"PAR3_3-way_partition\data_out.txt"

def main():
    with open(FILEPATH) as file:
        data = file.read().strip().splitlines()

    _ = int(data[0])
    array = list(map(int, data[1].split()))

    q = array[0]
    left, middle, right = [], [], [q]
    for k in array[1:]:
        if k < q:
            left.append(k)
        elif k >= q:
            right.append(k)
        else:
            middle.append(k)
    
    left.extend(middle)
    left.extend(right)

    with open(FILEPATH_WRITE, "w") as file:
        file.write(" ".join(map(str, left)))

if __name__ == "__main__":
    main()