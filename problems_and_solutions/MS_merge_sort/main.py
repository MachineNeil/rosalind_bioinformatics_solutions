'''
Problem

The problem of sorting a list of numbers lends itself immediately to a divide-and-conquer strategy: split the list into two halves, recursively sort each half, and then merge the two sorted sublists (recall the problem “Merge Two Sorted Arrays”).

Source: Algorithms by Dasgupta, Papadimitriou, Vazirani. McGraw-Hill. 2006.

Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105.

Return: A sorted array A[1..n].
Sample Dataset

10
20 19 35 -18 17 -20 20 1 4 4

Sample Output

-20 -18 1 4 4 17 19 20 20 35
'''

FILEPATH_READ = r"MS_merge_sort\data.txt"
FILEPATH_WRITE = r"MS_merge_sort\data_out.txt"

def merge_sort(array):
    l_a = len(array)
    middle = l_a / 2
    result = [""]

    if l_a == 1:
        return array
    
    first_half, second_half = merge_sort(array[:middle]), merge_sort(array[middle:])

    a, b = 0, 0

    while len(first_half) > a and len(second_half) > b:
        e_a, e_b = first_half[a], second_half[b]
        if e_a > e_b:
            result.append(e_b)
            b += 1
        else:
            result.append(e_a)
            a += 1
    
    result += first_half[a:] + second_half[b:]

    return result


def main():
    with open(FILEPATH_READ) as file:
        _ = int(next(file).strip())
        array = list(map(int, next(file).strip().split()))

    sorted_array = merge_sort(array)
    
    with open(FILEPATH_WRITE, "w") as file:
        file.write(" ".join(map(str, sorted_array)))

if __name__ == "__main__":
    main()