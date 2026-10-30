#leetcode 239. Sliding Window Maximum

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:

        q = deque()  # store indices of elements in the current window
        result = []

        for i in range(len(nums)):
            # Remove indices that are out of the current window
            if q and q[0] < i - k + 1:
                q.popleft()

            # Remove elements from the back of the deque that are smaller than the current element
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            # Add the current element's index to the deque
            q.append(i)

            # Append the maximum element of the current window to the result list
            if i >= k - 1:
                result.append(nums[q[0]])

        return result