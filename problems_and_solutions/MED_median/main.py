'''
Problem

The task is to implement a linear time randomized algorithm for the selection problem.

Given: A positive integer n≤105 and an array A[1..n] of integers from −105 to 105, a positive number k≤n.

Return: The k-th smallest element of A.

Source: Algorithms by Dasgupta, Papadimitriou, Vazirani. McGraw-Hill. 2006.
Sample Dataset

11
2 36 5 21 8 13 11 20 5 4 1
8

Sample Output

13
'''

import random

FILEPATH = r"MED_median\data.txt"
FILEPATH_WRITE = r"MED_median\data_out.txt"

def selection(array, k):
    if len(array) == 1:
        return array[0]
    
    v = random.choice(array)

    left, middle, right = [], [], []
    for i in array:
        if i < v:
            left.append(i)
        elif i > v:
            right.append(i)
        else:
            middle.append(i)
        
    if k <= len(left):
        return selection(left, k)
    elif k < len(left) + len(middle):
        return k
    else:
        return selection(right, k - len(left) - len(middle))

def main():
    with open(FILEPATH) as file:
        data = file.read().strip().splitlines()
    
    _ = int(data[0])
    array = list(map(int, data[1].split()))
    k = int(data[2])

    print(selection(array, k))

if __name__ == "__main__":
    main()