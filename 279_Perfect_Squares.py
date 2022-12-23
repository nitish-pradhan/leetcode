'''
Given an integer n, return the least number of perfect square numbers that sum to n.
A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. 
For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
'''

def numSquares(n: int) -> int:
    def helper(n):
        if n == 0:
            return 0
        if n < 0:
            return float('inf')
        if dp[n] != -1:
            return dp[n]

        least_square = n
        idx = 1
        while idx*idx <= n:
            least_square = min(least_square, helper(n-idx*idx))
            idx += 1

        dp[n] = least_square+1
        return dp[n]
        
    dp = [-1 for i in range(n+1)]
    return helper(n)

print(numSquares(13))