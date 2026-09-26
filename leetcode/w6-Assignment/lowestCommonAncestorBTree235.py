#leetcode 235. Lowest Common Ancestor of a Binary Search Tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root:'TreeNode', p:'TreeNode', q:'TreeNode') -> 'TreeNode':
        # strategy is observing one subtree at a time recursively
        #base case
        if root is None:
            return None

        #if both p and q are smaller than root, then LCA lies in left subtree
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        #if both p and q are greater than root, then LCA lies in right subtree
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        #if one of p or q is smaller than root and the other is greater than root
        else:
            return root

## Time complexity is O(h) where h is the height of the tree.
#SPACE COMPLEXITY IS O(h) where h is the height of the tree due to the recursion stack.

#Testcases
if __name__ == '__main__':

    #root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5]
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)

    # Testcase 1: LCA of nodes in different subtrees
    p = root.left  # Node with value 2
    q = root.right  # Node with value 8

    solution = Solution()
    lca = solution.lowestCommonAncestor(root, p, q)
    print(f"The lowest common ancestor of nodes {p.val} and {q.val} is: {lca.val}")  # Output: 6

    #testcase2, LCA on left subtree
    p = root.left
    q = root.left.right  # Node with value 4
    lca = solution.lowestCommonAncestor(root, p, q)
    print(f"The lowest common ancestor of nodes {p.val} and {q.val} is: {lca.val}")  # Output: 2

    #testcase3, LCA on right subtree
    p = root.right.left  # Node with value 7
    q = root.right.right  # Node with value 9
    lca = solution.lowestCommonAncestor(root, p, q)
    print(f"The lowest common ancestor of nodes {p.val} and {q.val} is: {lca.val}")  # Output: 8

    #testcase4, LCA is one of the nodes
    p = root.left.right.left  # Node with value 3
    q = root.left.right.right  # Node with value 5
    lca = solution.lowestCommonAncestor(root, p, q)
    print(f"The lowest common ancestor of nodes {p.val} and {q.val} is: {lca.val}")  # Output: 4