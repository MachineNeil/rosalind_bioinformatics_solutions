'''
Problem
Figure 4. A figure illustrating the propagation of Fibonacci's rabbits if they die after three months.

Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, which followed the recurrence relation Fn=Fn−1+Fn−2 and assumed that each pair of rabbits reaches maturity in one month and produces a single pair of offspring (one male, one female) each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).

Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.
Sample Dataset

6 3

Sample Output

4
'''

FILEPATH = r"FIBD_mortal_fibonacci_rabbits\data.txt"

def main():
    with open(FILEPATH) as file:
        n, m = map(int, file.read().strip().split())

    ages = [0] * m
    ages[0] = 1

    for _ in range(n - 1):
        newborns = sum(ages[2:])
        ages = [newborns] + ages[::-1]
        print(ages)

    print(sum(ages))

if __name__ == "__main__":
    main()