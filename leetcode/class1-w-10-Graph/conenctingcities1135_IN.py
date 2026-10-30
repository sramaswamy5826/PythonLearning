#leetcode 1135. Connecting Cities With Minimum Cost
# There are n cities numbered from 1 to n. You are given an array connections where connections[i] = [xi, yi, costi] indicates that the cost of connecting city xi and city yi is costi. Return the minimum cost to connect all the n cities such that there is exactly one path between each pair of cities. If it is impossible to connect all the n cities
import heapq
import List

class UF:
    def init__(self, n):
        self.parents = [i for i in range(n)]
        self.ranks = [i for i in range(n)]

    def find(self, node):
        while node != self.parents[node]:
            self.parents[node] = self.parents[self.parents[node]]
            node = self.parents[node]
        return node

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 == root2:
            return False
        if self.ranks[root1] > self.ranks[root2]:
            self.parents[root2] = root1
        elif self.ranks[root1] < self.ranks[root2]:
            self.parents[root1] = root2
        else:
            self.parents[root2] = root1
            self.ranks[root1] += 1
        return True

def min_cost(city_count: int, connections: List[List[int]]) -> int:
    costs = []
    for u, v, cost in connections:
        costs.append((cost, u - 1, v - 1))  # Convert to 0-based index

    print(connections)
    heapq.heapify(costs)
    print(costs)

    uf = UF(city_count)
    edge_count = 0
    min_cost = 0

    while costs and edge_count < city_count:
        smallest_cost, u, v = heapq.heappop(costs)
        if uf.union(u, v):
            edge_count += 1
            min_cost +=smallest_cost

    return min_cost if edge_count == city_count else -1





