'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
'''

'''
Intuition:
We start at either step 0 or step 1. The target is to reach either last or second last step, whichever is minimum.
Step 1 - Identify a recurrence relation between subproblems. In this problem,
Recurrence Relation:
    mincost(i) = cost[i]+min(mincost(i-1), mincost(i-2))
Base cases:
    mincost(0) = cost[0]
    mincost(1) = cost[1]
'''

def minCostClimbingStairs(cost: list) -> int:
    def get_cost(cost:list, step:int) -> int:
        if step < 0:
            return 0
        if step == 0 or step == 1:
            return cost[step]
        if dp.get(step):
            return dp[step]
        dp[step] =  cost[step] + min(get_cost(cost, step-1), get_cost(cost, step-2))
        return dp[step]
        
    dp = dict()
    return min(get_cost(cost, len(cost)-1), get_cost(cost, len(cost)-2))

min_cost = minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1])
print(min_cost)