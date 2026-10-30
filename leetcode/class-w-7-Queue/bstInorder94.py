#leetcode 94.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversalStack(self, root: TreeNode|None) -> list[int]:
        # Iterative approach using a stack
        result = []
        stack = []
        current = root

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result

    def inorderTraversal(self, root: TreeNode|None) -> list[int]:
        # Recursive approach:
        # usually neater, but can be less efficient due to function call overhead and stack space usage.

        result = []

        def helper(node: TreeNode|None):
            if not node:
                return
            helper(node.left)
            result.append(node.val)
            helper(node.right)

        helper(root)
        return result

#timeComplexity: O(n) where n is the number of nodes in the tree, since we visit each node once.
#spaceComplexity: O(n) where n is the number of nodes in the tree,

#Testcases
if __name__ == '__main__':
    # Testcase 1: Example tree
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    solution = Solution()
    result = solution.inorderTraversal(root)
    print(result)  # Output: [1, 3, 2]

    result_stack = solution.inorderTraversalStack(root)
    print(result_stack)  # Output: [1, 3, 2]

    # Testcase 2: Single node tree
    root = TreeNode(1)
    result = solution.inorderTraversal(root)
    print(result)  # Output: [1]

    result_stack = solution.inorderTraversalStack(root)
    print(result_stack)  # Output: [1]

    # Testcase 3: Empty tree
    root = None
    result = solution.inorderTraversal(root)
    print(result)  # Output: []

    result_stack = solution.inorderTraversalStack(root)
    print(result_stack)  # Output: []