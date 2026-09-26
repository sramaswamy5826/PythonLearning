#leetcode 104. Maximum Depth of Binary Tree
# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# A leaf is a node with no children.

class TreeNode:
    def __init__(self, v=0, left=None, right=None):
        self.val = eval
        self.left = left
        self.right = right

class Solution:
    def maxDepthRecursive(self, root:TreeNode|None) -> int:
        #using dfs traversal: recursive approach
        if root is None:
            return 0
        else:
            left_depth = self.maxDepthRecursive(root.left)
            right_depth = self.maxDepthRecursive(root.right)
            return max(left_depth, right_depth) + 1

#Time complexity: O(n) ->  n is the number of nodes in the tree
#Space complexity: O(h) -> h is the height of the tree, which is the maximum depth of the tree.

    def maxDepthIterative(self, root:TreeNode|None) -> int:
        if root is None:
            return 0

        #using stack for iterative depth first search (DFS) traversal
        stack = [(root, 1)]
        max_depth = 0
        while stack:
            node, depth = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
        return max_depth

#Time complexity: O(n) ->  n is the number of nodes in the tree
#Space complexity: O(h) -> h is the height of the tree, which is the


#Testcases
if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    sol = Solution()
    print(sol.maxDepthRecursive(root))
    print(sol.maxDepthIterative(root))

    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.left.left = TreeNode(3)
    sol = Solution()
    print(sol.maxDepthRecursive(root))
    print(sol.maxDepthIterative(root))