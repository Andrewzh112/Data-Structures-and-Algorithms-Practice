class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# Flatten Binary Tree to Linked List
class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def __init__(self):
        self.last_node = None
    def flatten(self, root):
        self.helper(root)

    def helper(self, node):
        if node is None:
            return node
        
        leftLast = self.helper(node.left)
        rightLast = self.helper(node.right)
        
        if leftLast is not None:
            leftLast.right = node.right
            node.right = node.left
            node.left = None
        if rightLast is not None:
            return rightLast
        if leftLast is not None:
            return leftLast
        return node

    def flatten2(self, node):
        if node is None:
            return node
        
        if self.last_node is not None:
            self.last_node.left = None
            self.last_node.right = node
        
        self.last_node = node
        right = node.right
        self.flatten2(node.left)
        self.flatten2(right)


# Invert Binary Tree
class Solution1:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def invertBinaryTree(self, root):
        # write your code here
        if root is None:
            return root
        
        right = root.right
        root.right = root.left
        root.left = right
        self.invertBinaryTree(root.left)
        self.invertBinaryTree(root.right)

    def invertBinaryTree2(self, root):
        # write your code here
        self.helper(root)
        
    def helper(self, node):
        if node is None:
            return node
        
        leftnode = self.helper(node.left)
        rightnode = self.helper(node.right)
        
        node.left = rightnode
        node.right = leftnode
        return node


# Binary Search Tree Iterator
class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        # do intialization if necessary
        self.stack = []
        while root != None:
            self.stack.append(root)
            root = root.left

    """
    @return: True if there has next node, or false
    """
    def hasNext(self):
        # write your code here
        return len(self.stack) > 0

    """
    @return: return next node
    """
    def next(self):
        # write your code here
        node = self.stack[-1]
        if node.right is None:
            n = self.stack.pop()
            while self.stack and self.stack[-1].right == n:
                n = self.stack.pop()
        else:
            n = node.right
            while n != None:
                self.stack.append(n)
                n = n.left
        return node


# Kth Smallest Element in a BST
class Solution2:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # write your code here
        self.results = []
        self.helper(root, k)
        return self.results[k - 1].val
        
    def helper(self, root, k):
        if len(self.results) > k or root is None:
            return
        self.helper(root.left, k)
        self.results.append(root)
        self.helper(root.right, k)


# Closest Binary Search Tree Value
class Solution3:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # write your code here
        upper = root
        lower = root
        while root:
            if target > root.val:
                lower = root
                root = root.right
            elif target < root.val:
                upper = root
                root = root.left
            else:
                return root.val
        if abs(upper.val - target) <= abs(lower.val - target):
            return upper.val
        return lower.val