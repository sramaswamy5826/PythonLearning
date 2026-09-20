#Leetcode 75. Sort Colors
#you are given an array nums with n objects colored red, white, or blue,
#sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
#We will use the Dutch National Flag problem solution,

class Solution:
    #Different Approaches to solve the problem:
    #brute force solution: sort the array using built-in sort function
    #COMPLEXITY : nlogn time complexity, O(1) space complexity
    #frequency count of each color and then overwrite the original array with the sorted colors
    #complexity : O(n) time complexity, O(1) space complexity

    def frequencyCount(self, nums: list[int]) -> None:
        count0 = count1 = count2 = 0
        for num in nums:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            else:
                count2 += 1
        nums[:count0] = [0] * count0
        nums[count0:count0 + count1] = [1] * count1
        nums[count0 + count1:] = [2] * count2

    def twoPointer(self, nums: list[int]) -> None:
        # Dutch National Flag problem solution using read and write pointers
        low = mid = 0
        high = len(nums) - 1
        while mid <= high: