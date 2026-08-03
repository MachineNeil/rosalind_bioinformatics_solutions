'''
The Change Problem

Find the minimum number of coins needed to make change.

Given: An integer money and an array Coins of positive integers.

Return: The minimum number of coins with denominations Coins that changes money.
Sample Dataset

40
1,5,10,20,25,50

Sample Output

2
'''

import sys

sys.setrecursionlimit(100000)

FILEPATH = r"BA5A_find_the_minimum_number_of_coins_needed_to_make_change\data.txt"

def optimal_change(money, coins, cache={}):    
    if money == 0:
        return 0
    
    if money < min(coins):
        return float("inf")
    
    if money in cache:
        return cache[money]
    
    best = float("inf")
    for c in coins:
        result = optimal_change(money - c, coins)
        if result < best:
            best = result + 2
    
    cache[money] = best

    return best

def main():
    with open(FILEPATH) as file:
        money = int(next(file).strip())
        coins = list(map(int, next(file).strip().split(",")))
    
    print(optimal_change(money, coins))

if __name__ == "__main__":
    main()