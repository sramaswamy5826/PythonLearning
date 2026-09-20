#leetcode 70. Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Given an integer n, return the number of distinct ways you can climb to the top.
# You can assume that 1 <= n <= 45.
class Solution:
    def climbRecursive(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbRecursive(n - 1) + self.climbRecursive(n - 2)

    def climbStairs_iterative(self, n: int) -> int:
        if n <= 2:
            return n
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b
        return b

#testcases
if __name__ == '__main__':
    solution = Solution()
    print(solution.climbStairs_iterative(2))  # Expected output: 2
    print(solution.climbStairs_iterative(3))  # Expected output: 3
    print(solution.climbStairs_iterative(4))  # Expected output: 5

    # complexity analysis for climbStairs_iterative: O(n) time complexity, O(1) space complexity
    # space complexity is O(1) because we are using only two variables to store the previous two results.