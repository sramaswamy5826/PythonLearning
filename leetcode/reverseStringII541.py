# leetcode 541. Reverse String II
# Given S and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # Convert the string to a list of characters for easier manipulation
        chars = list(s)
        n = len(chars)

        # Iterate over the string in steps of 2k
        for i in range(0, n, 2 * k):
            # Reverse the first k characters in the current 2k block
            chars[i:i + k] = reversed(chars[i:i + k])

        # Convert the list back to a string and return
        return ''.join(chars)

#testcase to validate the solution
if __name__ == "__main__":
    solution = Solution()
    # Test case 1
    s1 = "abcdefg"
    k1 = 2
    print(s1, "->", solution.reverseStr(s1, k1), "\n")  # Expected output: "bacdfeg"

    # Test case 2
    s2 = "abcd"
    k2 = 2
    print(s2, "->", solution.reverseStr(s2, k2), "\n")  # Expected output: "bacd"

    # Test case 3
    s3 = "a"
    k3 = 1
    print(s3, "->", solution.reverseStr(s3, k3), "\n")  # Expected output: "a"

    # Test case 4
    s4 = "abcdefghij"
    k4 = 3
    print(s4, "->", solution.reverseStr(s4, k4), "\n")  # Expected output: "cbadefihgj"

    # Test case 5
    s5 = "abcdef"
    k5 = 4
    print(s5, "->", solution.reverseStr(s5, k5), "\n")  # Expected output: "dcbaef"


#Complexity analysis:
# Time complexity: O(n), where n is the length of the string s.
# Space complexity: O(n) We convert the string to a list of characters for easier manipulation, which requires additional space proportional to the size of the input string.
