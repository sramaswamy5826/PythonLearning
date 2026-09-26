#Leetcode 20. Valid Parentheses

class Solution:
    def isValid(self, s:str) -> bool:
        if s is None or len(s) == 0:
            return True
        #HashMap and Stack approach
        # use dictionary to store the mapping of parentheses
        mapping = {')': '(', '}': '{', ']': '['}

        stack = []
        for char in s:
            if char in mapping:
                if not stack: return False #stack can be empty if the first character is a closing bracket
                top_element = stack.pop()
                if mapping[char]!=top_element:
                    return False
            else:
                stack.append(char)

        return not stack

#tescases
if __name__ == '__main__':
    sol = Solution()
    str1 = "()"
    print(str1, '->', sol.isValid(str1 ))

    str2="()[]{}"
    print(str2, '->', sol.isValid(str2))

    str3="(]"
    print(str3, '->', sol.isValid(str3))

    str4="([])"
    print(str4, '->', sol.isValid(str4))

    str5="([)]"
    print(str5, '->', sol.isValid(str5))

    str6="{[]}"
    print(str6, '->', sol.isValid(str6))

    str7="((()))"
    print(str7, '->', sol.isValid(str7))

    str8="((())"
    print(str8, '->', sol.isValid(str8))

    str9=""
    print(str9, '->', sol.isValid(str9))

    str10="}"
    print(str10, '->', sol.isValid(str10))

    str11="}{"
    print(str11, '->', sol.isValid(str11))


