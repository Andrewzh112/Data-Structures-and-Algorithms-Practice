from collections import deque
"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        # write your code here
        if not grid or not grid[0]:
            return -1
        
        seen = set()
        queue = deque()
        queue.append(source)
        seen.add((source.x, source.y))
        steps = 0
        
        while queue:
            size = len(queue)
            for _ in range(size):
                point = queue.popleft()
                x, y = point.x, point.y
                if (x, y) == (destination.x, destination.y):
                    return steps
                for direction in [[1,2],[1,-2],[-1,2],[-1,-2],[2,1],[2,-1],[-2,1],[-2,1]]:
                    newx = x + direction[0]
                    newy = y + direction[1]
                    if self.isvalid(newx, newy, grid, seen):
                        seen.add((newx, newy))
                        queue.append(Point(newx,newy))
            steps += 1
        return -1
        
    def isvalid(self, x, y, grid, seen):
        return 0 <= x <= len(grid) - 1 \
        and 0 <= y <= len(grid[0]) - 1 \
        and not grid[x][y] \
        and (x, y) not in seen