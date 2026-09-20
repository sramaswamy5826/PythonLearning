#leetcode 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
class Solution:

    #validate using counting approach
    def isValidCounting(self, s: str) -> bool:
        count = {'(': 0, ')': 0, '{': 0, '}': 0, '[': 0, ']': 0}
        for char in s:
            if char in count:
                count[char] += 1
        return count['('] == count[')'] and count['{'] == count['}'] and count['['] == count[']']



    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack