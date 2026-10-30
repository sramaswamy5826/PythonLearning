#leetcode 98. Validate Binary Search Tree
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:

        #level by level traversal, keeps track of range of valid values for each node, if any node is out of range, return False
        def is_valid(node: TreeNode | None, low=float('-inf'), high=float('inf')) -> bool:
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return is_valid(node.left, low, node.val) and is_valid(node.right, node.val, high)

        return is_valid(root)

        def inorder(node: TreeNode | None) -> list[int]: