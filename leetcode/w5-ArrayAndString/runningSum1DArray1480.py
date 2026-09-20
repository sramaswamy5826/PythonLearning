#leetcode 1480. Running Sum of 1d Array
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.
from typing import List

class Solution:
    # prefix sum approach
    def runningSum(self, nums:List[int])->List[int]:
        if nums is None or len(nums) == 0:
            return []
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums

#Testcases
if __name__ == "__main__":
    solution = Solution()
    print(solution.runningSum([1, 2, 3, 4]))  # Output: [1, 3, 6, 10]
    print(solution.runningSum([1, 1, 1, 1, 1]))  # Output: [1, 2, 3, 4, 5]
    print(solution.runningSum([3, 1, 2, 10, 1]))  # Output: [3, 4, 6, 16, 17]

#Time complexity: O(n), where n is the length of the input array.
#Space complexity: O(1)