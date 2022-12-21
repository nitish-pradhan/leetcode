
'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each 
of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
'''

'''
Intuition:
So it boils down to calculating what is more profitable:

 - robbery of current house + loot from houses before the previous
 - loot from the previous house robbery and any loot captured before that

 rob(i) = max(rob(i-2)+currentHouseValue, rob(i-1))

'''

# Time and Space - O(n)

def rob(nums: list) -> int:
    def helper(nums, n):
        if n < 0:
            return 0
        if dp[n] != -1:
            return dp[n]

        dp[n] = max(nums[n]+helper(nums, n-2), helper(nums, n-1))
        return dp[n]
        
    n = len(nums)
    dp = [-1 for i in range(n+1)]
    return helper(nums, n-1)

profit = rob([2,7,9,3,1])
print(profit)