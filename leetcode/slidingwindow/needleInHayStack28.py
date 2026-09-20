#leetcode 28. Implement strStr()
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# Clarification:
# What should we return when needle is an empty string? This is a great question to ask during an interview.
# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
class Solution:
    def bruteForceStrStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        needle_length = len(needle)
        haystack_length = len(haystack)
        for i in range(haystack_length - needle_length + 1):
            for j in range(needle_length):
                if haystack[i + j] != needle[j]:
                    break
            else:
                return i
        return -1
    
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        needle_length = len(needle)
        haystack_length = len(haystack)
        for i in range(haystack_length - needle_length + 1):
            if haystack[i:i + needle_length] == needle:
                return i
        return -1

    # Complexity analysis for strStr: O((N-L)L) time complexity, O(1) space complexity
    # where N is the length of haystack and L is the length of needle. The worst-case scenario occurs when we have to check every substring of haystack that has the same length as needle.