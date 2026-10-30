#leetcode 743. Network Delay Time

class Solution:
    # weighted directed graph, times[i] = (u, v, w)
    # Shortest time to reach all nodes from node k,
    # Dijkstra's algorithm can be used to find the minimum time it takes from node k to all other nodes.
    # If any node is unreachable, return -1.

    # Approaches:
    # BFS,DFS,Dijkstra's algorithm(no negative edges)

    #Dijkstra's algorithm
    def networkDelayTime(self , times:list[list[int]], n:int, k:int) -> int:
        from collections import defaultdict
        import heapq
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))  #store (neighbor, weight) in adjacency list

        # Min-heap to store (time, node)
        min_heap = [(0, k)]  # (time, node)
        # Dictionary to store the shortest time to reach each node
        shortest_time = {}

        while min_heap:
            time, node = heapq.heappop(min_heap)
            if node in shortest_time:
                continue
            shortest_time[node] = time

            for neighbor, weight in graph[node]:
                if neighbor not in shortest_time:
                    heapq.heappush(min_heap, (time + weight, neighbor))

        if len(shortest_time) == n:
            return max(shortest_time.values())
        return -1

#testcases
if __name__ == '__main__':
    s = Solution()
    print(s.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)) # Output: 2
    print(s.networkDelayTime([[1,2,1]], 2, 1)) # Output: 1
    print(s.networkDelayTime([[1,2,1]], 2, 2)) # Output: -1

#time complexity: O(E log V) where E is the number of edges and V is the number of vertices
#space complexity: O(V + E) for the graph representation and the shortest_time dictionary
