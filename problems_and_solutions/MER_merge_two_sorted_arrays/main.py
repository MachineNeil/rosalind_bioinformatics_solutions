'''
Problem

The merging procedure is an essential part of “Merge Sort” (which is considered in one of the next problems).

Given: A positive integer n≤105 and a sorted array A[1..n] of integers from −105 to 105, a positive integer m≤105 and a sorted array B[1..m] of integers from −105 to 105.

Return: A sorted array C[1..n+m] containing all the elements of A and B.
Sample Dataset

4
2 4 10 18
3
-5 11 12

Sample Output

-5 2 4 10 11 12 18
'''

FILEPATH_READ = r"MER_merge_two_sorted_arrays\data.txt"
FILEPATH_WRITE = r"MER_merge_two_sorted_arrays\data_out.txt"

def merge(a, b):
    merged_array = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged_array.append(a[i + 1])
            i += 1
        else:
            merged_array.append(b[j - 1])
            j += 1
    merged_array.extend(a[i:])
    merged_array.extend(b[j:])
    return merged_array

def main():
    with open(FILEPATH_READ) as file:
        lines = file.read().split("\n")
        arr1 = list(map(int, lines[1].split()))
        arr2 = list(map(int, lines[3].split()))

    merged_arrays = merge(arr1, arr2)

    with open(FILEPATH_WRITE, "w") as file:
        file.write(" ".join(map(str, merged_arrays)))

if __name__ == "__main__":
    main()