#leetcode383. Ransom Note
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Create a dictionary to count the frequency of each character in the magazine
        #example: char_count = {'a': 2, 'b': 1}
        char_count = {}

        # Count characters in the magazine
        for char in magazine:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        # Check if we can construct the ransom note
        for char in ransomNote:
            if char not in char_count or char_count[char] == 0:
                return False  # Not enough characters to construct the ransom note
            char_count[char] -= 1  # Use one occurrence of the character

        return True  # All characters needed for the ransom note are available

#Testcase to validate the solution
if __name__ == "__main__":
    solution = Solution()
    # Test case 1
    ransomNote1 = "a"
    magazine1 = "b"
    print(ransomNote1, magazine1, "->", solution.canConstruct(ransomNote1, magazine1))  # Expected output: False

    # Test case 2
    ransomNote2 = "aa"
    magazine2 = "ab"
    print(ransomNote2, magazine2, "->", solution.canConstruct(ransomNote2, magazine2))  # Expected output: False

    # Test case 3
    ransomNote3 = "aa"
    magazine3 = "aab"
    print(ransomNote3, magazine3, "->", solution.canConstruct(ransomNote3, magazine3))  # Expected output: True


#complexity Analysis:
#Time Complexity: O(n + m), where n is the length of ransomNote and m is the length of magazine. We traverse both strings once.
#Space Complexity: O(k), where k is the number of unique characters in magazine. In the worst case, k could be equal to the length of magazine.
