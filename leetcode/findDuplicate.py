#leetcode 287. Find the Duplicate Number
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.
from typing import List

class Solution:
    def findDuplicateBruteForce (self, nums: List[int]) -> int:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return nums[i]
        return -1

    #complexity analysis for findDuplicateBruteForce: O(n^2) time complexity, O(1) space complexity
    #space complexity is O(1) because we are not using any extra space, just a few variables for iteration.

    def findDuplicateSet(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1
    #complexity analysis for findDuplicateSet: O(n) time complexity, O(n) space complexity
    #space complexity is O(n) because we are using a set to store the seen numbers

    def findDuplicateHashMap(self, nums: List[int]) -> int:
        num_count = {}
        for num in nums:
            if num in num_count:
                return num
            num_count[num] = 1
        return -1

    #complexity analysis for findDuplicateHashMap: O(n) time complexity, O(n) space complexity
    #space complexity is O(n) because we are using a hash map to store the count

    def findDuplicateFloydsTortoiseAndHare(self, nums: List[int]) -> int:



