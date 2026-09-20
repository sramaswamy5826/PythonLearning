# leetcode 643. Maximum Average Subarray I
# Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.
from typing import List

# understand :
# Requirements Analysis:
# planing:
#   start with brute force approach, then optimize using sliding window technique.
#  Implementation:

class Solution:
    def averageOfSubarray(self, nums: List[int], k: int) -> float:
        n = len(nums)

        current_sum = sum(nums[:k])
        maxsum = current_sum

        for  j in range(1, n):

        numbers = [1, 2, 3, 4, 5]
        print(self.averageOfSubarray(numbers, 2))  # Output: 4.5