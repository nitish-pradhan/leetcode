'''
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window.

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

[-7,-8,7,5,7,1,6,0], k=3 => [7,7,7,7,7,6]

'''

from collections import deque

def maxSlidingWindow(nums: list, k: int) -> list:
    max_q = deque()
    result = list()
    start, end = 0, 0

    while end < len(nums):
        #Calclation
        while len(max_q) > 0 and nums[end] > max_q[-1]:
            #Pop smaller elements from last
            max_q.pop()
        max_q.append(nums[end])

        if end-start+1 < k:
            #Increase window size
            end += 1
        else:
            # Window size is matching
            result.append(max_q[0])
            end += 1

            if nums[start] == max_q[0]:
                max_q.popleft()
            start += 1
        
    return result

max_sliding_window = maxSlidingWindow([-7,-8,7,5,7,1,6,0], 3)
print(max_sliding_window)
