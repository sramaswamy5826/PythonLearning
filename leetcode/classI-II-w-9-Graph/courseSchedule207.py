#leetcode 207. Course Schedule
# There are a total of numCourses courses you have to take, labeled from 0 to

class Solution:
    #using recursive DFS to detect cycle in directed graph
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # Create an adjacency list to represent the graph
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        # States: 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses

        def has_cycle(v):
            if state[v] == 1:  # Found a cycle
                return True
            if state[v] == 2:  # Already visited
                return False

            state[v] = 1  # Mark as visiting
            for neighbor in graph[v]:
                if has_cycle(neighbor):
                    return True
            state[v] = 2  # Mark as visited
            return False

        for course in range(numCourses):
            if has_cycle(course):
                return False

        return True
