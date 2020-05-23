"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        self.BST = True
        self.last_node = None
        self.validateBST(root)
        return self.BST
        
    def validateBST(self,root):
        if root is None:
            return
        self.validateBST(root.left)
        if self.last_node is not None and self.last_node.val >= root.val:
            self.BST = False
            return
        self.last_node = root
        self.validateBST(root.right)