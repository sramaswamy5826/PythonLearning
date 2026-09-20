#leetcode 704. Binary Search
# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

from typing import List

class Solution:
    #recursive binary search
    def searchRecursive(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums) == 0:
            return -1
        # first call to the recursive function with initial left and right bounds
        return self._searchRecursive(nums, target, left=0, right=len(nums) - 1)

    def _searchRecursive(self, nums: List[int], target: int, left: int, right: int) -> int:
        if left > right:
            return -1
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            #search in the right half of the array
            return self._searchRecursive(nums, target, mid + 1, right)
        else:
            #search in the left half of the array
            return self._searchRecursive(nums, target, left, mid - 1)

#Time complexity: O(log n), where n is the number of elements in the array. This is because with each recursive call, the search space is halved.
#Space complexity: O(n) due to the recursion stack.

    #iterative binary search
    def search(self, nums: List[int], target: int) -> int:
        if nums is None or len(nums) == 0:
             return -1

        left, right=0, len(nums)-1
        while left <= right:
            mid = left+(right-left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
               left = mid+1
            else:
                right = mid-1
        return -1

#Time complexity: O(log n), where n is the number of elements in the array. With each iteration the search space is halved.
#Space complexity: O(1) because of constant space.

#testcases
if __name__ == "__main__":
    solution = Solution()

    #Recursive binary search test cases
    print('Recursive binary search test cases:')
    print(solution.searchRecursive([-1, 0, 3, 5, 9, 12], 9))  # Output: 4
    print(solution.searchRecursive([-1, 0, 3, 5, 9, 12], 2))  # Output: -1
    print(solution.searchRecursive([1, 3, 5, 6], 5))  # Output: 2
    print(solution.searchRecursive([1, 3, 5, 6], 2))  # Output: -1
    print(solution.searchRecursive([1, 3, 5, 6], 7))  # Output: -1
    print(solution.searchRecursive([1, 3, 5, 6], 0))  # Output: -1

    #iterative binary search test cases
    print('Iterartive binary search test cases:')
    print(solution.search([-1, 0, 3, 5, 9, 12], 9))  # Output: 4
    print(solution.search([-1, 0, 3, 5, 9, 12], 2))  # Output: -1
    print(solution.search([1, 3, 5, 6], 5))  # Output: 2
    print(solution.search([1, 3, 5, 6], 2))  # Output: -1
    print(solution.search([1, 3, 5, 6], 7))  # Output: -1
    print(solution.search([1, 3, 5, 6], 0))  # Output: -1