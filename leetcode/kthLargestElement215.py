#Leetcode 215.  Kth Largest Element in an Array

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        #using quickselect algorithm, Hoare's partition algorithm since it handles duplicates better, less swaps and is more efficient than Lomuto's partition algorithm

        target_index = len(nums) - k

        left=0
        right=len(nums)-1

        while left<right:
            boundary_index = self.partition(nums, left, right)
            if target_index < boundary_index:
                right = boundary_index - 1
            else:
                left = boundary_index + 1

        return nums[left]  # when left == right, return the element at that index

    @staticmethod
    def partition(nums, left, right)->int:
        pivot = nums[left+(right-left)//2]
        i=left
        j=right

        while i<=j:
            while nums[i]<pivot:
                i+=1
            while nums[j]>pivot:
                j-=1
            if i<=j:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
        return i  # return the index

#testcase to validate the solution
if __name__ == "__main__":
    solution = Solution()
    # Test case 1
    nums1 = [3,2,1,5,6,4]
    k1 = 2
    print(nums1, k1, "->", solution.findKthLargest(nums1, k1))  # Expected output: 5

    # Test case 2
    nums2 = [3,2,3,1,2,4,5,5,6]
    k2 = 4
    print(nums2, k2, "->", solution.findKthLargest(nums2, k2))  # Expected output: 4

    # Test case 3
    nums3 = [1]
    k3 = 1
    print(nums3, k3, "->", solution.findKthLargest(nums3, k3))  # Expected output: 1

    #COMPLEXITY ANALYSIS
    #Time complexity: O(n) on average, O(n^2) in the worst
    #space complexity: O(1) since we are doing in-place partitioning