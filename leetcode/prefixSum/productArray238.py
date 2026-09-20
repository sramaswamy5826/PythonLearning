# leetcode 3238. Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.
from typing import List

class Solution:

    def productExceptSelf(self, nums:List[int])->List[int]:
        n = len(nums)
        res = [1] * n  # Initialize the result array with 1s

        # Calculate prefix products
        prefix_product = 1
        for i in range(n):
            res[i] = prefix_product
            prefix_product *= nums[i]

        # Calculate postfix products and multiply with the result
        postfix_product = 1
        for i in range(n - 1, -1, -1):
            res[i] *= postfix_product
            postfix_product *= nums[i]

        return res
    def productExceptSelf_brute(self, nums:list[int])->list[int]:
        n = len(nums)

        res = []
        prefix = [1]
        for i in range(len(nums)-1):
            prefix.append(prefix[-1] * nums[i])

        print(prefix)
        postfix = [1 for _ in range(len(nums))] #initialize postfix array with 1s
        for i in range(len(nums)-2, -len(nums)-1, -1):
            postfix[i] = postfix[i+1] * nums[i+1]

        for pre, post in zip(prefix, postfix):
            res.append(pre * post)

        return res

# timeComplexity: O(n) where n is the length of the input array. We traverse the array three times: once for prefix, once for postfix, and once to compute the result.
# spaceComplexity: O(n) where n is the length of the input array. We
# use two additional arrays (prefix and postfix) of size n to store the prefix and postfix products.



#testcases
if __name__ == "__main__":
    solution = Solution()
    numbers = [-1, 1, 0, -3, 3]
    print(solution.productExceptSelf(numbers))