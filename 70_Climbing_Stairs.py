'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

'''

# Intuition - If we can reach to [n-1] or [n-2] steps then from there we need just one step to reach the top.
# We should calculate different ways to reach n-1 and n-2 steps and to reach n steps will be summation of both.
# For memoization we just need to keep track of the ways we have counted.

def climbStairs(n: int) -> int:
    def helper(n:int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        if memo.get(n):
            return memo[n]
        
        memo[n] = helper(n-1) + helper(n-2)
        return memo[n]

    memo = {1:1, 2:2}
    return helper(n)

print('Different ways - ', climbStairs(15))