#leetcode 103. Binary Tree Zigzag Level Order Traversal
# Given the root of a binary tree, return the zigzag level order traversal of its nodes'
# values. (i.e., from left to right, then right to left for the next level and alternate between).

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode|None) -> list[list[int]]:
        # Breath first traversal/Level order traversal,
        # instead of list using deque since pop(0) is O(n) in list but popleft() is O(1) in deque, also it's cleaner
        if not root:
            return []
        result = []
        queue = deque([root])
        left_to_right = True  # Flag to track the direction of traversal

        while queue:
            level_size = len(queue)
            level_nodes = []
            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if not left_to_right:
                level_nodes.reverse()  # Reverse the order for right-to-left traversal
            result.append(level_nodes)
            left_to_right = not left_to_right  # Toggle the direction for the next level

        return result

#timeComplexity: O(n) where n is the number of nodes in the tree, since we visit each node once.
#spaceComplexity: O(n) where n is the number of nodes in the tree, since we store the nodes in the queue and the result list.

#Testcases
if __name__ == '__main__':
    # Testcase 1: Example tree
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solution = Solution()
    result = solution.zigzagLevelOrder(root)
    print(result)  # Output: [[3], [20, 9], [15, 7]]

    # Testcase 2: Single node tree
    root = TreeNode(1)
    result = solution.zigzagLevelOrder(root)
    print(result)  # Output: [[1]]

    # Testcase 3: Empty tree
    root = None
    result = solution.zigzagLevelOrder(root)
    print(result)  # Output: []