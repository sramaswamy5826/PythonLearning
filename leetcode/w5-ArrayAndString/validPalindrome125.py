# leetcod #125. Valid Palindrome
#1, Convert uppercase letters into lowercase letters.
#2, Remove all non-alphanumeric characters.
#3, Reads same forward and backward.

class Solution:
    def palindrome(self, s: str) -> bool:
        # Convert the string to lowercase and filter out non-alphanumeric characters
        filteredChars = [char.lower() for char in s if char.isalnum()]

        # Check if the filtered list of characters is the same forwards and backwards
        return filteredChars == filteredChars[::-1]

#Testcase to validate the solution
if __name__ == "__main__":
    solution = Solution()
    # Test case 1
    s1 = "A man, a plan, a canal: Panama"
    print(s1, "->", solution.palindrome(s1), "\n")  # Expected output: True

    # Test case 2
    s2 = "race a car"
    print(s2, "->", solution.palindrome(s2), "\n")  # Expected output: False

    # Test case 3
    s3 = " "
    print(s3, "->", solution.palindrome(s3), "\n")  # Expected output: True

#TimeComplexity : O(n), where n is the length of the input string s.
#Space Complexity: O(n), to store n filtered list chars

