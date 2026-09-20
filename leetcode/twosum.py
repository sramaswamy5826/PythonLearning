#leetcode #1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
from typing import List

class Solution:
    def twoSum(self, nums:List, target:int)->tuple[int,int]:
        num_to_index = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return (num_to_index[complement], index)
            num_to_index[num] = index
        return None

    def twoSumBruteForce(self, nums:List, target:int)->tuple[int,int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return (i, j)
        return None

    def twoSumTwoPointer(self, nums:List, target:int)->tuple[int,int]:
        nums_with_index = [(num, index) for index, num in enumerate(nums)]
        nums_with_index.sort(key=lambda x: x[0])
        left, right = 0, len(nums_with_index) - 1
        while left < right:
            current_sum = nums_with_index[left][0] + nums_with_index[right][0]
            if current_sum == target:
                return (nums_with_index[left][1], nums_with_index[right][1])
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return None

#Improved: using hash map to store the complement of each number and its index, allowing for O(n) time complexity. The brute force method checks all pairs of numbers, resulting in O(n^2) time complexity. The two-pointer method requires sorting the array first, leading to O(n log n) time complexity, but it uses O(n) space to store the original indices.
    def twoSum(self, nums:List[int], target:int)->tuple[int,int]:
        num_to_index = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return (num_to_index[complement], index)
            num_to_index[num] = index
        return None


# #complexity analysis for twoSumBruteForce: O(n^2) time complexity, O(1) space complexity
    #complexity analysis for twoSum: O(n) time complexity, O(n) space complexity
    #complexity analysis for twoSumTwoPointer: O(nlogn) time complexity, O(n) space complexity