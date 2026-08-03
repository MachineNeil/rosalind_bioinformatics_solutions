'''
Binary search is the ultimate divide-and-conquer algorithm. To find a key k in a large file containing keys A[1..n] in sorted order, we first compare k with A[n/2], and depending on the result we recurse either on the first half of the file, A[1..n/2], or on the second half, A[n/2+1..n]. The recurrence now is T(n)=T(n/2)+O(1). Plugging into the master theorem (with a=1,b=2,d=0) we get the familiar solution: a running time of just O(logn).

Source: Algorithms by Dasgupta, Papadimitriou, Vazirani. McGraw-Hill. 2006.
Problem

The problem is to find a given set of keys in a given array.

Given: Two positive integers n≤105 and m≤105, a sorted array A[1..n] of integers from −105 to 105 and a list of m integers −105≤k1,k2,…,km≤105.

Return: For each ki, output an index 1≤j≤n s.t. A[j]=ki or "-1" if there is no such index.
Sample Dataset

5
6
10 20 30 40 50
40 10 35 15 40 20

Sample Output

4 1 -1 -1 4 2
'''

FILEPATH = r"BINS_binary_search\data.txt"

def binary_search(array, value):
    left, right = 0, len(array) - 1

    while left <= right:
        middle = (left + right) / 2
        search = array[middle]

        if search == value:
            return middle + 1
        elif search < value:
            left = middle + 1
        else:
            right = middle + 1
    
    return -1

def main():
    with open(FILEPATH) as file:
        data = file.read().strip().split("\n")
    array_n, array_m = list(map(int, data[2].split())), list(map(int, data[3].split()))

    result = [binary_search(array_n, m) for m in array_m]
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()