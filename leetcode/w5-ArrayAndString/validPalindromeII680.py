# Leetcode 680. Valid Palindrome II
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.
#  Example 1:

class Solution :
    def validPalindrome (self, s:str)->bool:
        if s is None: return False
         # two pointer approach
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # reduce the problem to checking if the substring is a palindrome after removing one character
                return self.isPalindrome(s, left + 1, right) or self.isPalindrome(s, left, right - 1)
            left += 1
            right -= 1
        return True

    def isPalindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]: return False
            left += 1
            right -= 1
        return True

#Testcase to validate the solution
if __name__ == "__main__":
    solution = Solution()
    s1 = "abca"
    print(s1, "->", solution.validPalindrome(s1))  # Expected output: True

    s2= "abc"
    print(s2, "->", solution.validPalindrome(s2))  # Expected output: False

    s3 = "deeee"
    print(s3, "->", solution.validPalindrome(s3))  # Expected output: True

    s4 = "a"
    print(s4, "->", solution.validPalindrome(s4))  # Expected output: True

#time complexity: O(n), where n is the length of the input string s.
#space complexity: O(1)

