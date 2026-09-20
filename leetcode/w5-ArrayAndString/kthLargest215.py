# leetcode 215. Kth Largest Element in an Array
# Given an integer array nums and an integer k, return the kth largest element in the array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
import heapq
class Solution:
    def findKthLLargest(self, nums:list[int], k:int)->int:
        # Previous solved with QuickSelect approach in W4,
        # So solving using a min-heap to keep track of the k largest elements
        # Min-heap - root has the smallest element, will always have the k largest elements.
        if len(nums) < k:
            return -1
        min_heap = [] # list to store the k largest elements
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]  # The root of the min-heap is the kth largest element

#Testcase to validate the solution
if __name__ == "__main__":
    solution = Solution()
    print(solution.findKthLLargest([3,2,1,5,6,4], 2))  # Expected output: 5
    print(solution.findKthLLargest([3,2,3,1,2,4,5,5,6], 4))  # Expected output: 4
    print(solution.findKthLLargest([3,2,3,1,2,4,5,5,6], 1))  # Expected output: 6
    print(solution.findKthLLargest([0, 0, 0], 4))  # Expected output: -1
    print(solution.findKthLLargest([-4, -2, 3], 2))  # Expected output: -2

#Time complexity: O(n log k), where n -> number of elements in the array. Each insertion into the heap takes O(log k) time, and we do this for all n elements.
#Space complexity: O(k), since we are storing k elements in the heap.


