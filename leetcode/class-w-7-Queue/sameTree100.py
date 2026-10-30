#leetcode 100. Same Tree
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursion or Iteration ?
# Traversal : BFS, DFS(PREORDER, INORDER, POSTORDER) ?
class Solution:
    def isSameTreeRecursive(self, p:TreeNode|None, q:TreeNode|None)->bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val: # node ->left -> right
            return False
        return self.isSameTreeRecursive(p.left, q.left) and self.isSameTreeRecursive(p.right, q.right)

    def isSameTreeBFS(self, p:TreeNode|None, q:TreeNode|None)->bool:
        from collections import deque
        queue = deque([(p, q)])
        while queue:
            node1, node2 = queue.popleft()
            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            queue.append((node1.left, node2.left))
            queue.append((node1.right, node2.right))
        return True