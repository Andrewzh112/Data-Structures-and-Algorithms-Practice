from queue import Queue


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class UndirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []


# Binary Tree Level Order Traversal
class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        results = []
        if root is None:
            return results
        queue = Queue()
        queue.put(root)
        while not queue.empty():
            size = queue.qsize()
            result = []
            for _ in range(size):
                node = queue.get()
                result.append(node.val)
                if node.left is not None:
                    queue.put(node.left)
                if node.right is not None:
                    queue.put(node.right)
            results.append(result)
        return results


# Binary Tree Level Order Traversal II
class Solution2:
    """
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def levelOrderBottom(self, root):
        results = []
        if root is None:
            return results
        
        queue = Queue()
        queue.put(root)
        while not queue.empty():
            size = queue.qsize()
            result = []
            for _ in range(size):
                node = queue.get()
                result.append(node.val)
                if node.left is not None:
                    queue.put(node.left)
                if node.right is not None:
                    queue.put(node.right)
            results.append(result)
        return list(reversed(results))


# Serialize and Deserialize Binary Tree
class Solution3:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        results = []
        if root is None:
            return results
        queue = Queue()
        queue.put(root)
        while not queue.empty():
            node = queue.get()
            if node is None:
                results.append('#')
            else:
                results.append(node.val)
                queue.put(node.left)
                queue.put(node.right)
        return results
                
                    
    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """
    def deserialize(self, data):
        fast, slow = 0, 0
        if len(data) == 0: return
        root = data[slow] = TreeNode(data[slow])
        while fast < len(data) - 1:
            node = data[slow]
            if node is None:
                slow += 1
                continue
            fast += 1
            if data[fast] == '#':
                node.left = data[fast] = None
            else:
                node.left = data[fast] = TreeNode(data[fast])
            fast += 1
            if data[fast] == '#':
                node.right = data[fast] = None
            else:
                node.right = data[fast] = TreeNode(data[fast])
            slow += 1
        return root


# Binary Tree Zigzag Level Order Traversal
class Solution4:
    """
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        l2r = 0
        results = []
        if root is None: return results
        queue = Queue()
        queue.put(root)
        while not queue.empty():
            size = queue.qsize()
            result = []
            for _ in range(size):
                node = queue.get()
                result.append(node.val)
                if node.left is not None:
                    queue.put(node.left)
                if node.right is not None:
                    queue.put(node.right)
            if l2r % 2:
                result = list(reversed(result))
            l2r += 1
            results.append(result)
        return results


# Convert Binary Tree to Linked Lists by Depth
class Solution5:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):
        # Write your code here
        results = []
        if root is None: return results
        queue = Queue()
        queue.put(root)
        treenode = root
        while not queue.empty():
            size = queue.qsize()
            dummy = node = ListNode(None)
            for _ in range(size):
                treenode = queue.get()
                node.next = node = ListNode(treenode.val)
                if treenode.left is not None:
                    queue.put(treenode.left)
                if treenode.right is not None:
                    queue.put(treenode.right)
            results.append(dummy.next)
        return results


# Clone Graph
class Solution6:
    """
    @param node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        # write your code here
        root = node
        if root is None:
            return root
            
        nodes = self.get_nodes(root)
        
        mapping = {}
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node.label)
        
        for node in nodes:
            for neighbor in node.neighbors:
                mapping[node].neighbors.append(mapping[neighbor])
        
        return mapping[root]
    
    def get_nodes(self, root):
        nodes = set([root])
        queue = Queue()
        queue.put(root)
        while not queue.empty():
            node = queue.get()
            nodes.add(node)
            for neighbor in node.neighbors:
                if neighbor not in nodes:
                    queue.put(neighbor)
                    nodes.add(neighbor)
        return nodes
