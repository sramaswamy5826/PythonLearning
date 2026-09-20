# Leetcode 438. Find All Anagrams in a String
# Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
# An Anagram is a string formed by rearranging the letters of a different string, using all the original letters exactly once.
from collections import Counter  # dictionary to count the frequency of characters in p and s

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        # Base case: if the length of s is less than the length of p, return an empty list
        if len(s) < len(p) : return []

        # sliding window and freq map approach to find all anagrams of p in s
        pmap = {}
        smap = {}

        for ch in p:
            pmap[ch] = pmap.get(ch, 0) + 1

        for ch in s[:len(p)]:
            smap[ch] = smap.get(ch, 0) + 1

        result = []
        if smap == pmap:
            result.append(0)

        left = 0;
        for right in range(len(p), len(s)):
            smap[s[right]] = smap.get(s[right], 0) + 1

            smap[s[left]] -= 1
            if smap[s[left]] == 0:
                del smap[s[left]]
            left += 1

            if smap == pmap:
                result.append(left)

        return result

#Testcase to validate the solution
if __name__ == "__main__":
    solution = Solution()
    s1 = "cbaebabacd"
    p1 = "abc"
    print(s1, p1, "->", solution.findAnagrams(s1, p1))  # Expected output: [0, 6]

    s2 = "abab"
    p2 = "ab"
    print(s2, p2, "->", solution.findAnagrams(s2, p2))  # Expected output: [0, 1, 2]

    s3 = "af"
    p3 = "be"
    print(s3, p3, "->", solution.findAnagrams(s3, p3))  # Expected output: []

    s4 = "abc"
    p4 = "abcd"
    print(s4, p4, "->", solution.findAnagrams(s4, p4))  # Expected output: []

#Time complexity: O(n), where n is the length of the input string s.
#Space complexity: O(1), constant space is used for the frequency maps, as the number of unique characters is limited, with max 26 (lowercase).
