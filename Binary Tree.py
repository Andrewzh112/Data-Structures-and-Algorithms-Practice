class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


# Minimum Subtree
class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        self.min_node = None
        self.min_val = float('inf')
        self.find_min(root)
        return self.min_node
    
    def find_min(self, node):
        if node is None:
            return 0
            
        tree_sum = self.find_min(node.left) + self.find_min(node.right) + node.val
        if tree_sum <= self.min_val:
            self.min_val = tree_sum
            self.min_node = node
        return tree_sum
    
    # another way to solve the problem
    def findSubtree2(self, root):
        _, subtree, _ = self.find_smallest(root)
        return subtree
    
    def find_smallest(self, node):
        if node is None:
            return 0, None, float('inf')
        
        left_curr, left_min_node, left_min_sum = self.find_smallest(node.left)
        right_curr, right_min_node, right_min_sum = self.find_smallest(node.right)
        
        curr_sum = left_curr + right_curr + node.val
        
        if left_min_sum == min(left_min_sum, right_min_sum, curr_sum):
            return curr_sum, left_min_node, left_min_sum
        if right_min_sum == min(left_min_sum, right_min_sum, curr_sum):
            return curr_sum, right_min_node, right_min_sum
        return curr_sum, node, curr_sum

# Binary Tree Paths
class Solution2:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        results = []
        if root is None:
            return results
        self.helper(root, [str(root.val)], results)
        return results
    
    def helper(self, node, path, results):
        if node.left is None and node.right is None:
            results.append('->'.join(path))
            return
        
        if node.left:
            path.append(str(node.left.val))
            self.helper(node.left, path, results)
            path.pop()
        if node.right:
            path.append(str(node.right.val))
            self.helper(node.right, path, results)
            path.pop()


# Lowest Common Ancestor of a Binary Search Tree
class Solution3:
    """
    @param root: root of the tree
    @param p: the node p
    @param q: the node q
    @return: find the LCA of p and q
    """
    def lowestCommonAncestor(self, root, p, q):
        # write your code here
        if root == q or root == p or root is None:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left is not None and right is not None:
            return root
        if left is not None:
            return left
        if right is not None:
            return right
        return None


# Lowest Common Ancestor III
class Solution4:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        LCA, nodeA, nodeB = self.helper(root, A, B)
        
        if nodeA and nodeB:
            return LCA
        return None
    
    def helper(self, node, A, B):
        if node is None:
            return None, False, False
        
        leftLCA, leftnodeA, leftnodeB = self.helper(node.left, A, B)
        rightLCA, rightnodeA, rightnodeB = self.helper(node.right, A, B)
        
        nodeA = leftnodeA or rightnodeA or node == A
        nodeB = leftnodeB or rightnodeB or node == B
        
        if node == A or node == B:
            return node, nodeA, nodeB
        if leftLCA is not None and rightLCA is not None:
            return node, nodeA, nodeB
        if leftLCA is not None:
            return leftLCA, nodeA, nodeB
        if rightLCA is not None:
            return rightLCA, nodeA, nodeB
        return None, nodeA, nodeB
