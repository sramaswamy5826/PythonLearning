#leetcode 207. Course Schedule
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        #using Khans algorithm to detect cycle in directed graph
        #Tracking in-degrees of each course and using a queue to process courses with no prerequisites
        indegree = [0] * numCourses
        # dictionary to represent the graph, where each course points to its dependent courses
        # Example: {0: [], 1: [], 2: [], 3: []}
        adj = {i: [] for i in range(numCourses)}

        # build the graph and populate the in-degree array
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1

        # traverse the neighbors of each course and reduce the in-degree of dependent courses
        # If a dependent course's in-degree becomes 0, add it to the queue for processing
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0: queue.append(i)

        completed_courses = 0
        while queue:
            course = queue.popleft()
            completed_courses += 1

            for neighbor in adj[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return completed_courses == numCourses

## #testcases
if __name__ == '__main__':
    s = Solution()
    print(s.canFinish(2, [[1, 0]]))  # Output: True
    print(s.canFinish(2, [[1, 0], [0, 1]]))  # Output: False
    print(s.canFinish(4, [[1, 0], [2, 1], [3, 2]]))  # Output: True
    print(s.canFinish(3, [[0, 1], [1, 2], [2, 0]]))  # Output: False
    print(s.canFinish(5, [[1, 0], [2, 1], [3, 2], [4, 3]]))  # Output: True

#time complexity: O(V + E) where V is the number of courses and E is the number of prerequisites
#space complexity: O(V + E) for the adjacency list and in-degree array

