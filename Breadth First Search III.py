from collections import Counter
from heapq import heappush, heappop, heapify


# Alien Dictionary
class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        indegrees, graph = self._construct_graph(words)
        if graph is None:
            return ""
        all_letters = set(''.join(words))
        for letter in all_letters:
            if letter not in graph:
                graph[letter] = []

        queue = [node for node in graph if indegrees[node] == 0]
        heapify(queue)
        lexigraph = []
        while queue:
            letter = heappop(queue)
            lexigraph.append(letter)
            for next_letter in graph[letter]:
                indegrees[next_letter] -= 1
                if indegrees[next_letter] == 0:
                    heappush(queue, next_letter)
        print(lexigraph, all_letters)
        if len(lexigraph) == len(all_letters):
            return ''.join(lexigraph)
        return ""

    def _construct_graph(self, words):
        graph = {}
        indegrees = Counter()
        for word1, word2 in zip(words[:-1], words[1:]):
            for i in range(min(len(word1), len(word2))):
                letter1, letter2 = word1[i], word2[i]
                if letter1 != letter2:
                    if letter1 not in graph:
                        graph[letter1] = [letter2]
                    else:
                        graph[letter1].append(letter2)
                    indegrees[letter2] += 1
                    break
                if i == min(len(word1), len(word2)) - 1:
                    if len(word1) > len(word2):
                        return None, None
        return indegrees, graph


# Sequence Reconstruction
class Solution2:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        graph = self.build_graph(seqs)
        topo_order = self.topological_sort(graph)
        return topo_order == org
            
    def build_graph(self, seqs):
        graph = {}
        for seq in seqs:
            for node in seq:
                if node not in graph:
                    graph[node] = set()
        
        for seq in seqs:
            for i in range(1, len(seq)):
                graph[seq[i - 1]].add(seq[i])

        return graph
    
    def get_indegrees(self, graph):
        indegrees = Counter()
        for node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] += 1
        return indegrees
        
    def topological_sort(self, graph):
        indegrees = self.get_indegrees(graph)
        queue = []
        for node in graph:
            if indegrees[node] == 0:
                queue.append(node)
                
        # not queue because only 1 can exist in list at a time
        topo_order = [] 
        while queue:
            if len(queue) > 1:
                return False
                
            node = queue.pop()
            topo_order.append(node)
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
                    
        if len(topo_order) == len(graph):
            return topo_order
            
        return False