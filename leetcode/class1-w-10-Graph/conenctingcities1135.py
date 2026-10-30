#leetcode 1135. Connecting Cities With Minimum Cost
# There are n cities numbered from 1 to n. You are given an array connections where connections[i] = [xi, yi, costi] indicates that the cost of connecting city xi and city yi is costi. Return the minimum cost to connect all the n cities such that there is exactly one path between each pair of cities. If it is impossible to connect all the n cities
import List

class Solution:

    def minCostConnectionPointsKruskal(self, points: List[List[int]]) -> int:
        # Using Kruskal's algorithm to find the minimum spanning tree (MST) of the graph formed by the cities and their connection costs.
        parent = {}
        rank = {}

        def find(city):
            if parent[city] != city:
                parent[city] = find(parent[city])
            return parent[city]

        def union(city1, city2):
            root1 = find(city1)
            root2 = find(city2)

            if root1 != root2:
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                elif rank[root1] < rank[root2]:
                    parent[root1] = root2
                else:
                    parent[root2] = root1
                    rank[root1] += 1

        edges = []
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                cost = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append((cost, i, j))

        edges.sort()  # Sort edges based on cost

        for i in range(n):
            parent[i] = i
            rank[i] = 0

        total_cost = 0
        for cost, city1, city2 in edges:
            if find(city1) != find(city2):
                union(city1, city2)
                total_cost += cost

        return total_cost

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Using Prim's algorithm to find the minimum spanning tree (MST) of the graph formed by the cities and their connection costs.
        n = len(points)
        min_heap = [(0, 0)]  # (cost, city_index)
        total_cost = 0
        visited = set()

        while len(visited) < n:
            cost, city_index = heapq.heappop(min_heap)
            if city_index in visited:
                continue
            visited.add(city_index)
            total_cost += cost

            for next_city in range(n):
                if next_city not in visited:
                    next_cost = abs(points[city_index][0] - points[next_city][0]) + abs(points[city_index][1] - points[next_city][1])
                    heapq.heappush(min_heap, (next_cost, next_city))

        return total_cost

