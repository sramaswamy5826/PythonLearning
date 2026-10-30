#leetcode 1762. Find Buildings With an Ocean View
# There are n buildings in a line. You are given an integer array heights of size n where heights[i] is the height of the ith building.
# The ocean is to the right of all the buildings. A building has an ocean view if the building can see the ocean without obstructions.
# Formally, a building has an ocean view if all the buildings to its right have a height strictly less than the building's height. Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

class Solution:
    # Using monotonic stack, we can iterate from right to left and keep track of the maximum height seen so far. If the current building's height is greater than the maximum height, it has an ocean view.

    def findBuildings(self, heights: list[int]) -> list[int]:
        n = len(heights)
        result = []
        max_height = 0

        for i in range(n - 1, -1, -1):
            if heights[i] > max_height:
                result.append(i)
                max_height = heights[i]

        return result[::-1]  # Reverse the result to get indices in increasing order