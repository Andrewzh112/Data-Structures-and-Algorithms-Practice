from collections import deque
"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        top_order = []
        
        indegrees = {node:0 for node in graph}
        for node in graph:
            for neighbor in node.neighbors:
                indegrees[neighbor] += 1
        
        queue = deque()
        for node in indegrees:
            if indegrees[node] == 0:
                queue.append(node)
        
        while queue:
            node = queue.popleft()
            top_order.append(node)
            for neighbor in node.neighbors:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        return top_order