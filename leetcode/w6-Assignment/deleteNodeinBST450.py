#leetcode 450. Delete Node in a BST

"""
case:
1. Node has no children
2. Node has one child
3. Node has two children

"""


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root:TreeNode|None, key:int) -> TreeNode|None:
        #base case, if the root is None, return None
        if not root:
            return None

        # If the key to be deleted is smaller than the root's value, then it lies in the left subtree
        if key < root.value:
            root.left = self.deleteNode(root.left, key)
        # If the key to be deleted is greater than the root's value, then it lies in the right subtree
        elif key > root.value:
            root.right = self.deleteNode(root.right, key)
        else:
            #found the node to be deleted
            # Node with only one child or no child
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # Node with two children: Find Inorder Successor
            # Get the inorder successor (smallest in the right subtree)
            temp = root.right
            while temp.left:
                temp = temp.left

            root.value = temp.value
            root.right = self.deleteNode(root.right, temp.value)
        return root

#timeComplexity: O(h) where h is the height of the tree, since we traverse from the root to the node to be deleted.
#spaceComplexity: O(h) where h is the height of the tree, due to the recursion stack.

#Testcases
if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)

    #Testcase1: Deleting a node with two children
    solution = Solution()
    new_root = solution.deleteNode(root, 3)
    # Expected output: [5, 4, 6, 2, None, None, 7]
    print(new_root.value)  # Output: 5
    print(new_root.left.value)  # Output: 4
    print(new_root.right.value)  # Output: 6
    print(new_root.left.left.value)  # Output: 2
    print(new_root.right.right.value)  # Output: 7
    print()

    # Testcase 2: Deleting a leaf node
    new_root = solution.deleteNode(root, 2)
    # Expected output: [5, 4, 6, None, None, None, 7]
    print(new_root.value)  # Output: 5
    print(new_root.left.value)  # Output: 4
    print(new_root.right.value)  # Output: 6
    print(new_root.left.left)  # Output: none
    print(new_root.left.right)  # Output: none
    print(new_root.right.left)  # Output: none
    print(new_root.right.right.value)  # Output: 7
    print()

    # Testcase 3: Deleting a node with one child
    new_root = solution.deleteNode(root, 6)
    # Expected output: [5, 4, 7, None, None, None, None]
    print(new_root.value)  # Output: 5
    print(new_root.left.value)  # Output: 4
    print(new_root.right.value)  # Output: 7
    print(new_root.left.left)  # Output: none
    print(new_root.left.right)  # Output: none
    print(new_root.right.left)  # Output: none
    print(new_root.right.right)  # Output: none

