#leetcode 133. Clone Graph

"""
 Steps:
 1.Requirements
 2. Input and Output
 3. Make Plan
    datastructure, how to solve, what to return

    Solution:
    1. Use DFS to traverse the graph and clone each node.
"""

class Node:
    def __init__(self, val = 0, neighbors = list[int]) - :
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        # Dictionary to save the visited nodes and their clones
        visited = {}

        def dfs(n):
            if n in visited:
                return visited[n]

            # Clone the node
            clone = Node(n.val)
            visited[n] = clone

            # Iterate through the neighbors to generate their clones
            for neighbor in n.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)
