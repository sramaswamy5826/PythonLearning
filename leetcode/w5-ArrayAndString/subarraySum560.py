# leetcode 560. Subarray Sum Equals K
# Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #sliding window approach does not work here because the array can contain negative numbers, which can cause the sum to decrease as we expand the window. Therefore, prefix sum approach instead.
        #prefix sum approach
        count = 0
        prefix_sum = 0
        prefix_sum_map = {0: 1}  # Initialize with prefix sum 0 having one occurrence

        for num in nums:
            prefix_sum += num
            if (prefix_sum - k) in prefix_sum_map:
                count += prefix_sum_map[prefix_sum - k]
            prefix_sum_map[prefix_sum] = prefix_sum_map.get(prefix_sum, 0) + 1

        return count

#Testcases
if __name__ == "__main__":
    solution = Solution()
    print(solution.subarraySum([1, 1, 1], 2))  # Output: 2
    print(solution.subarraySum([1, 2, 3], 3))  # Output: 2
    print(solution.subarraySum([1, -1, 0], 0))  # Output: 3
    print(solution.subarraySum([3, 4, 7, 2, -3, 1, 4, 2], 7))  # Output: 4

#Time complexity: O(n), where n is the length of the input array.
#Space complexity: O(n), where n is the number of unique prefix sum - HashMap
