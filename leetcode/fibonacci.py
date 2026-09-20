# leetcode #509. Fibonacci Number
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.
# Given n, calculate F(n).
class Solution:

    def bruteForceFib(self, n)->int:
        if n<=1:
            return n
        return self.bruteForceFib(n-1) + self.bruteForceFib(n-2)

    #complexity analysis for bruteForceFib: O(2^n) time complexity, O(n) space complexity due to the recursion stack.
    #why 2^n time complexity? Because each call to bruteForceFib results in two more calls, leading to an exponential growth in the number of calls as n increases.

    def fibMeomoization(self, n, memo={})->int:
        if n in memo:
            return memo[n]
        if n<=1:
            return n
        memo[n] = self.fibMeomoization(n-1, memo) + self.fibMeomoization(n-2, memo)
        return memo[n]
    # complexity analysis for fibMeomoization: O(n) time complexity, O(n) space complexity due to the memo dictionary.


    def fib(self, n)->int:
        if n<=1:
            return n
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b

    # complexity analysis for fib: O(n) time complexity, O(1) space complexity

    def fib(self):