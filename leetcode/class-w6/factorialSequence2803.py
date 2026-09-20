#leetcode 2830. Factorial Sequence
# The factorial sequence is defined as follows:
# F(0) = 1
# F(1) = 1
# F(n) = n * F(n - 1) for n > 1.
# Given an integer n, return the value of F(n).
class Solution:
    def factorialSequence(self, n: int) -> int:
        if n <= 1:
            return 1
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result