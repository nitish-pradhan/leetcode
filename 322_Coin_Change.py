'''
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Input: coins = [2], amount = 3
Output: -1
'''

# Intuition - Unbounded Knapsack : To choose or not to choose
# Time and Space: O(len(coins) * amount)

import math
def coinChange(coins: list, amount: int) -> int:
    def helper(coins: list, amount: int, pos: int) -> int:
        if amount == 0: # Found colution
            return 0
        if pos < 0: # Solution not possible
            return math.inf
        
        if dp[pos][amount] != -1:
            return dp[pos][amount]
        
        if coins[pos] <= amount:
            dp[pos][amount] = min(1 + helper(coins, amount-coins[pos], pos), helper(coins, amount, pos-1))
        else:
            dp[pos][amount] = helper(coins, amount, pos-1)
        
        return dp[pos][amount]

    coins = sorted(coins)
    dp = [ [-1 for col in range(amount+1)] for row in range(len(coins))]
    result = helper(coins, amount, len(coins)-1)
    return -1 if result == math.inf else result

print(coinChange([1,2,5], 11))
print(coinChange([2], 3))