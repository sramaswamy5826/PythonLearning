#leetcode 101. Symmetric Tree
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetricRecursive(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)

    def isMirror(self, left: TreeNode | None, right: TreeNode | None) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val) and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left)


    def isSymmetricIterative(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        from collections import deque
        queue = deque([(root.left, root.right)])

        #compare before adding to queue, rather than adding to queue and then comparing, since we can avoid adding unnecessary nodes to the queue
        while queue:
            left, right = queue.popleft()
            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False
            queue.append((left.left, right.right))
            queue.append((left.right, right.left))
        return True
