#leetcode 322. Coin Change
# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money. Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1
# You may assume that you have an infinite number of each kind of coin.

class Solution:
    #top-down dynamic programming with memoization
    def coinChange(self, coins: list[int], amount: int) -> int:
        # Create a memoization dictionary to store the minimum coins needed for each amount
        memo = {}

        def dp(n):
            # Base case: if the amount is 0, no coins are needed
            if n == 0:
                return 0
            # If the amount is negative, return -1 (not possible)
            if n < 0:
                return -1
            # If we have already computed the result for this amount, return it
            if n in memo:
                return memo[n]

            min_coins = float('inf')
            for coin in coins:
                res = dp(n - coin)
                if res >= 0 and res < min_coins:
                    min_coins = res + 1

            # Store the result in the memoization dictionary
            memo[n] = -1 if min_coins == float('inf') else min_coins
            return memo[n]

        return dp(amount)

    #bottom-up dynamic programming
    def coinChangeBottomUp(self, coins: list[int], amount: int) -> int:
        # Create a DP array to store the minimum coins needed for each amount
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins are needed to make amount 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return -1 if dp[amount] == float('inf') else dp[amount]