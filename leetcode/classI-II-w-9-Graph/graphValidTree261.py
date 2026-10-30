#leetcode 261. Graph Valid Tree
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.
from lib2to3.pgen2.pgen import DFAState


class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors

""" Make a plan
1. DFS vs BFS
2. Recursive vs Iterative
3. Data Structure used

Union find is the best solution for undirected graph cycle detection, but we can also use BFS or DFS to detect cycles in undirected graph.
"""

class Solution:
        # not disconnected, and no cycles, and all nodes are connected
        # cycle detection

        # Build the graph using adjacency List before traversal
        # Since this checks for a valid treem tracking visited nodes is sufficient(PATH TRACKING ISN'T NEEDED FOR tree validation)
        #It is best to use set for keeping track of visited nodes, as it provides O(1) average time complexity for membership checks and insertions. This is important for efficiency, especially when dealing with larger graphs.
        #Track the parent of each node to avoid treating the undirected back-edge to the parent as a cycle. If we encounter a visited node that is not the parent, it indicates a cycle.
        #Simply traversing the graph is not enough to prove it is a tree, we also need to check if all nodes are connected. This can be done by checking if the number of visited nodes equals n after the traversal.

        def validTree(self, n: int, edges: list[list[int]]) -> bool:
            if len(edges) != n - 1:
                return False

            from collections import defaultdict, deque

            graph = defaultdict(list)
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)

            visited = set()
            queue = deque([0])
            visited.add(0)

            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            return len(visited) == n

    def recursiveDFS(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        from collections import defaultdict

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(node, parent):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if not dfs(neighbor, node):
                        return False
                elif neighbor != parent:
                    return False
            return True

        if not dfs(0, -1):
            return False

        return len(visited) == n

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]

    def find(self, node):
        while node != self.parent[node]:
            node = self.parent[self.parent[node]]

    def union(self, node1, node2):



def is_graph_valid_tree(n:int, edges:list[list[int]]) -> bool:
    unionFind = UnionFind(n)
    if u,v in edges:
        if unionFind.find(u) == unionFind.find(v): return false
        unionFind.union(u, v)

