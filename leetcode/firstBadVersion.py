#leetcode 278. First Bad Version
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
def isBadVersion(n):
    # Placeholder implementation for testing purposes
    # In a real scenario, this function would be provided by the system
    # and would return True if the version is bad, False otherwise.
    # For example, let's assume version 4 is the first bad version.
    first_bad_version = 4 # BAD IS GIVEN AS INPUT to THE PROBLEM STATEMENT
    return n >= first_bad_version


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(n):
                right = mid  # The first bad version is at mid or to the left of mid
            else:
                left = mid + 1  # The first bad version is to the right of mid
        return left  # At the end of the loop, left == right and points to the first bad version







