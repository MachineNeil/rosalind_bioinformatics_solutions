'''
Problem

An inversion of an array A[1..n] is a pair of indices (i,j) such that 1≤i<j≤n and A[i]>A[j]. The number of inversions shows how far the array is from being sorted: if it is already sorted then there are no inversions, whereas if it is sorted in reverse order then the number of inversions is maximal.

Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105.

Return: The number of inversions in A.
Sample Dataset

5
-6 1 15 8 10

Sample Output

2
'''

FILEPATH = r"INV_counting_inversions\data.txt"

def merge_sort(array):
    result = []

    if len(array) == 1:
        return array, 0

    middle = len(array) / 2
    first_half, left_count = merge_sort(array[:middle])
    second_half, right_count = merge_sort(array[middle:])

    count = left_count + right_count
    a, b = 0, 0

    while a < len(first_half) and b < len(second_half):
        e_a = first_half[a]
        e_b = second_half[b]
        if e_a <= e_b:
            result.append(e_a)
            a += 1
        else:
            result.append(e_b)
            b += 1
            count += len(first_half) - a

    result += first_half[a:] + second_half[b:]

    return result, count

def main():
    with open(FILEPATH) as file:
        _ = int(next(file).strip())
        array = list(map(int, next(file).strip().split()))

    _, count = merge_sort(array)
    print(count)
    
if __name__ == "__main__":
    main()