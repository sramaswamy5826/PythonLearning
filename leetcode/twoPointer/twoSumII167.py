#leetcode 167. Two Sum II - Input Array Is Sorted
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing

class Solution:
    def twoSum(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                return [left + 1, right + 1] #  found, return
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        return []  # Return an empty list if no solution is found
