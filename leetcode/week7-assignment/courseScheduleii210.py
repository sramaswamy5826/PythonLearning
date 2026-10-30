#leetcode 210. Course Schedule II
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# For example, the pair [0, 1], indicates that to take course 0 you have to
# first take course 1. Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

class Solution:
    """
        Directed Graph,
        Different Approaches:
            1. Topological Sort using Kahn's Algorithm (BFS) - using Queue and indegree array
            2. Topological Sort using DFS - using recursion and visited array
            3. DFS - iterative using stack
    """
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # using BFS approach since it is cleaner and models prerequisites as indegrees and produces a valid topological order.
        #Choosing BFS since the output is about ordering of courses.
        from collections import defaultdict, deque

        # Create a graph and an indegree array
        graph = defaultdict(list)
        indegree = [0] * numCourses

        # Build the graph and fill the indegree array
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1

        # Initialize a queue with all courses that have no prerequisites
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []

        while queue:
            course = queue.popleft()
            order.append(course)

            # Decrease the indegree of neighboring courses
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                # If indegree becomes zero, add it to the queue
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        # If we were able to take all courses, return the order; otherwise, return an empty array
        return order if len(order) == numCourses else []

# Testcases
if __name__ == '__main__':
    s = Solution()
    print(s.findOrder(2, [[1, 0]]))  # Output: [0, 1]
    print(s.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))  # Output: [0, 1, 2, 3] or [0, 2, 1, 3]
    print(s.findOrder(1, []))  # Output: [0]
    print(s.findOrder(3, [[1, 0], [2, 1], [0, 2]]))  # Output: [] (cycle)

#Time Complexity: O(V + E) V- verties, E- edges
#Space Complexity: O(V + E) for graph and indegree array
