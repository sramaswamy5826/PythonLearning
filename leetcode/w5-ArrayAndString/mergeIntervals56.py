# leetcode 56   . Merge Intervals
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        #sort the intervals based on the start time
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]] #initialize with the first interval

        for current in intervals[1:]:
            if current[0] <= merged[-1][1]: #end value of last interval in merged list
                # update the end value of last interval in merged list
                merged[-1][1] = max(merged[-1][1], current[1])
            else:
                merged.append(current)
        return merged

#Testcase to validate the solution
if __name__ == '__main__':
    solution = Solution()
    # Test case 1
    intervals1 = [[1,3],[2,6],[8,10],[15,18]]
    print(intervals1, "->", solution.merge(intervals1))  # Expected output: [[1,6],[8,10],[15,18]]

    # Test case 2
    intervals2 = [[1,4],[4,5]]
    print(intervals2, "->", solution.merge(intervals2))  # Expected output: [[1,5]]

    # Test case 3
    intervals3 = [[1,4],[0,4]]
    print(intervals3, "->", solution.merge(intervals3))  # Expected output: [[0,4]]

    # Test case 4
    intervals4 = [[1,4],[0,0]]
    print(intervals4, "->", solution.merge(intervals4))  # Expected output: [[0,0],[1,4]]

    # Test case 5
    intervals5 = [[1,2],[4, 6], [7,10]]
    print(intervals5, "->", solution.merge(intervals5))  # Expected output: [[1,2],[4,6],[7,10]]

    #Complexity analysis:
    # Time complexity: O(n log n), where n is the number of intervals.
    # Space complexity: O(n), where n is the number of intervals.
