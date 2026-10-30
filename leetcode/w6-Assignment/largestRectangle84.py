#leetcode 84. Largest Rectangle in Histogram
class Solution:
    """
        1. if current height is greater than right height it can be extended
        2. if current height is less than right height, it can't be extended
        3. if current height is equal to right height, it can be extended
        4. Consider example: [1, 2, 3, 4, 3]
            keep advancing right since current height is less than right height
            when we reach 4,
            1. we can't extend it to the right since 3 is less than 4,
            2. so we pop 4 and calculate area with width 1

        using stack - (height and index)

    """
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = [] # pair(index, height)
        maxArea = 0
        heights.append(0)  # Append a zero height to pop all remaining bars in the stack

        for i, h in enumerate(heights):
            start = i;
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height*(i-index))
                start = index
            stack.append((start, h))

        #Items still in stack will be popped and area calculated
        for i, h in stack:
            maxArea = max(maxArea, h*(len(heights)-i))
        return maxArea

#time complexity: O(n)
#space complexity: O(n)

#TESTCASES
s = Solution()
print(s.largestRectangleArea([2,1,5,6,2,3]))

print(s.largestRectangleArea([1]))

print(s.largestRectangleArea([1, 2, 3, 4, 5]))

print(s.largestRectangleArea([5, 4, 3, 2, 1]))



