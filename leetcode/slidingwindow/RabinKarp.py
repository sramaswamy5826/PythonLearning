#RabinKarp - falls under sliding window because it uses hashing to find a substring in a string. It is not a sliding window algorithm because it does not use a fixed-size window to slide over the input string. Instead, it uses a rolling hash to compute the hash value of the substring and compare it with the hash value of the pattern.
# It is a hashing-based algorithm used to find whether a pattern appears in a text, or to compare substrings efficiently.
# Common use cases:
# • Searching for a pattern in a text
# ◦ Example: find "abc" inside "xabcxyz"
# • Detecting duplicate substrings
# • Comparing large strings efficiently
# • Network/security tools where substring checks are frequent
# • Some plagiarism or content scanning systems

# Typical complexity:
# •
# Average time: O(n + m)
# •
# Worst-case: O(n * m) if hash collisions are bad
# •
# Space: O(1) extra (for rolling hash, usually)
# Important note:
# •
# It is most useful when you want to search for many patterns or when you can use rolling hash efficiently.
# •
# For simple single pattern searches, Python’s built-in in is often easier and faster in practice.