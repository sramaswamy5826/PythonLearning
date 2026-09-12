# leetcode 443. String Compression
# Given an array of characters chars, compress it using the following algorithm:
# Begin with an empty string s. For each group of consecutive repeating characters in chars:
# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.
# After you are done modifying the input array, return the new length of the array
# You must write an algorithm that uses only constant extra space.

class Solution(object):
    def stringCompression(self, s):

        n = len(s)
        if n == 0:
            return 0

        write_index = 0
        read_index = 0

        while read_index < n:
            current_char = s[read_index]
            count = 0

            # Count the number of occurrences of the current character
            while read_index < n and s[read_index] == current_char:
                read_index += 1
                count += 1

            # Write the character to the array
            s[write_index] = current_char
            write_index += 1

            # If the count is greater than 1, write the count as well
            if count > 1:
                for digit in str(count):
                    s[write_index] = digit
                    write_index += 1

        return write_index

# TESTCASES
if __name__ == "__main__":
    solution = Solution()
    # Test case 1
    chars1 = ["a", "a", "b", "b", "c", "c", "c"]
    new_length1 = solution.stringCompression(chars1)
    print(chars1[:new_length1], "-> New length:", new_length1)  # Expected output: ["a", "2", "b", "2", "c", "3"] -> New length: 6

    # Test case 2
    chars2 = ["a"]
    new_length2 = solution.stringCompression(chars2)
    print(chars2[:new_length2], "-> New length:", new_length2)  # Expected output: ["a"] -> New length: 1

    # Test case 3
    chars3 = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    new_length3 = solution.stringCompression(chars3)
    print(chars3[:new_length3], "-> New length:", new_length3)  # Expected output: ["a", "b", "1", "0"] -> New length: 4


#Complexity analysis:
# Time complexity: O(n), where n is the length of the input array chars.
# Space complexity: O(1)

