#leetcode 124. Binary Tree Maximum Path Sum
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf') #negative infinity to handle negative values in the tree

        def helper(node):
            # base case: if the node is None, return 0
            if not node:
                return 0

            # Recursively get the maximum gain from left and right subtrees
            left_gain = max(helper(node.left), 0)  # Only consider positive gains
            right_gain = max(helper(node.right), 0)

            # Current path sum including the current node
            current_path_sum = node.val + left_gain + right_gain

            # Update the global maximum path sum if the current path sum is greater
            self.max_sum = max(self.max_sum, current_path_sum)

            # Return the maximum gain that can be obtained by including the current node
            return node.val + max(left_gain, right_gain)

        helper(root)
        return self.max_sum

#Testcases
if __name__ == "__main__":
    # Example test case
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    print(Solution().maxPathSum(root))  # Output: 6

    # Additional test case with negative values
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().maxPathSum(root))  # Output: 42

    # Edge case with all negative values
    root = TreeNode(-3)
    print(Solution().maxPathSum(root))  # Output: -3

#Time complexity: O(N) where N is the number of nodes in the tree, since we visit each node once.
#Space complexity: O(H) where H is the height of the tree, for recursion stack. In the worst case (skewed tree), H can be equal to N.

