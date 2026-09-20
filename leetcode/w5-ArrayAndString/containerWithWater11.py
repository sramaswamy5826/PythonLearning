# leetcode 11. Container With Most Water
# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line
# i is at (i, ai) and (i, 0). Find two lines, which together with the x-axis forms a container, such that the container contains the most water.
class Solution:
    def maxArea(self, height:list[int]) -> int:
        #two pointer approach
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the area formed by the lines at the left and right pointers
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height
            max_area = max(max_area, current_area)

            # Move the pointer pointing to the shorter line inward
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

#testcase to validate the solution
if __name__ == "__main__":
    solution = Solution()
    height1 = [1,8,6,2,5,4,8,3,7]
    print(height1, "->", solution.maxArea(height1))  # Expected output: 49

    height2 = [1,1]
    print(height2, "->", solution.maxArea(height2))  # Expected output: 1

    height3 = [4,3,2,1,4]
    print(height3, "->", solution.maxArea(height3))  # Expected output: 16

    height4 = [1,2,1]
    print(height4, "->", solution.maxArea(height4))  # Expected output: 2

    height5 = [1,2,4,3]
    print(height5, "->", solution.maxArea(height5))

    height6 = [5,4,3,2,1]
    print(height6, "->", solution.maxArea(height6))

    height7 = [1,0]
    print(height7, "->", solution.maxArea(height7))

#Time complexity: O(n), where n is the number of elements in the input list height.
#Space complexity: O(1), constant space is used.