import collections
from queue import Queue


class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class UndirectedGraph:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


# Word Ladder
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        dict.add(end)
        queue = collections.deque([start])
        seen = set([start])
        
        distance = 0
        while queue:
            distance += 1
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == end:
                    return distance

                for next_word in self.get_neighbors(word):
                    if next_word not in dict or next_word in seen:
                        continue
                    queue.append(next_word)
                    seen.add(next_word) 
        return 0

    def get_neighbors(self, word):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                if word[i] == char:
                    continue
                words.append(left + char + right)
        return words


# Number of Islands
class Solution2:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        # write your code here
        num_islands = 0
        if not grid:
            return num_islands
        self.seen = set()
        self.height, self.width = len(grid), len(grid[0])
        for i in range(self.height):
            for j in range(self.width):
                if (i, j) in self.seen or grid[i][j] == 0:
                    continue
                num_islands += 1
                self.seen.add((i, j))
                self.bfs(i, j, grid)
        return num_islands

    def bfs(self, i, j, grid):
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        queue = Queue()
        queue.put((i, j))
        while not queue.empty():
            i, j = queue.get()
            for s in range(len(dx)):
                x = i + dx[s]
                y = j + dy[s]
                if self.isValid(x, y, grid):
                    self.seen.add((x, y))
                    queue.put((x, y))

    def isValid(self, i, j, grid):
        if i < 0 or i > self.height - 1:
            return False
        if j < 0 or j > self.width - 1:
            return False
        if (i, j) in self.seen:
            return False
        if grid[i][j] == 0:
            return False
        return True


# Knight Shortest Path
class Solution3:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        # write your code here
        num_steps = 0
        if not grid: return num_steps
        
        seen = set()
        i, j = source.x, source.y
        seen.add((i, j))
        queue = Queue()
        queue.put((i, j))
        
        dx = [1, 1, -1, -1, 2, 2, -2, -2]
        dy = [2, -2, 2, -2, 1, -1, 1, -1]

        while not queue.empty():
            size = queue.qsize()
            for _ in range(size):
                i, j = queue.get()
                if i == destination.x and j == destination.y:
                    return num_steps
                for s in range(len(dx)):
                    x = i + dx[s]
                    y = j + dy[s]
                    if self.isValid(x, y, grid, seen):
                        seen.add((x, y))
                        queue.put((x, y))
            num_steps += 1
        return -1

    def isValid(self, x, y, grid, seen):
        if x < 0 or x > len(grid) - 1:
            return False
        if y < 0 or y > len(grid[0]) - 1:
            return False
        if grid[x][y]:
            return False
        if (x, y) in seen:
            return False
        return True


# Topological Sorting
class Solution4:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        edges = {node: 0 for node in graph}
        for node in graph:
            for neighbor in node.neighbors:
                edges[neighbor] += 1
        
        queue = Queue()
        for node, num_edges in edges.items():
            if num_edges == 0:
                queue.put(node)
        results = []
        while not queue.empty():
            node = queue.get()
            results.append(node)
            for neighbor in node.neighbors:
                edges[neighbor] -= 1
                if edges[neighbor] == 0:
                    queue.put(neighbor)
        return results


# Course Schedule
class Solution5:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # write your code here
        indegrees = {}
        graph = {}
        for course, prereq in prerequisites:
            indegrees[course] = indegrees.get(course, 0) + 1
            if prereq in graph:
                graph[prereq].append(course)
            else:
                graph[prereq] = [course]
        
        queue = Queue()
        for course in range(numCourses):
            if course not in indegrees:
                queue.put(course)
            if course not in graph:
                graph[course] = []

        top_sort = []
        while not queue.empty():
            course = queue.get()
            top_sort.append(course)
            for req in graph[course]:
                indegrees[req] -= 1
                if indegrees[req] == 0:
                    queue.put(req)

        return len(top_sort) == numCourses


# Course Schedule II
class Solution6:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        indegrees = collections.Counter()
        graph = {}
        
        for course, prereq in prerequisites:
            indegrees[course] += 1
            if prereq in graph:
                graph[prereq].append(course)
            else:
                graph[prereq] = [course]
        
        queue = Queue()
        for course in range(numCourses):
            if indegrees[course] == 0:
                queue.put(course)
            if course not in graph:
                graph[course] = []
                
        top_sort = []
        while not queue.empty():
            course = queue.get()
            top_sort.append(course)
            for req in graph[course]:
                indegrees[req] -= 1
                if indegrees[req] == 0:
                    queue.put(req)
        if len(top_sort) == numCourses:
            return top_sort
        return []