#leetcode 1584. Min Cost to Connect All Points
# Given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi], return the minimum cost to make all points connected.

import  heapq

class Solution:
    # Minimum Spanning Tree - Prim's Algorithm.
    # Since we need to find the min cost to connect all points.

    def minCostConnectPoints(self, points: list[list[int]]) -> int:

        n = len(points)
        if n == 0:
            return 0

        # Function to calculate Manhattan distance (given in the problem statement)
        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        # Prim's algorithm
        min_heap = [(0, 0)]  # (cost, point_index)
        visited = set()
        result = 0

        while len(visited) < n:
            cost, i = heapq.heappop(min_heap)
            if i in visited:
                continue
            visited.add(i)
            result += cost #min cost is always chosen from the min_heap, so we add it to the result
            for j in range(n):
                if j not in visited:
                    distance = manhattan(points[i], points[j])
                    edge = (distance, j)
                    heapq.heappush(min_heap, edge)
        return result
# Time complexity: O(n^2 log n) where n is the number of points.
# The outer loop runs n times, and for each point, we may push up to n edges into the heap(n^2), and each push/pop operation takes O(log n).
# Space complexity: O(n) for the min_heap and visited set.

#Testcases
if __name__ == '__main__':
    s = Solution()
    print(s.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]])) # Output: 20
    print(s.minCostConnectPoints([[3,12],[-2,5],[-4,1]])) # Output: 18
    print(s.minCostConnectPoints([[0,0],[1,1],[1,0],[-1,1]])) # Output: 4
    print(s.minCostConnectPoints([[0,0]])) # Output: 0
    print(s.minCostConnectPoints([[1,2],[3,4],[5,6]])) # Output: 8



