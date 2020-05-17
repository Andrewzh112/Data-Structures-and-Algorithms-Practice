from collections import deque
class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """

    def numIslands(self, grid):
        # write your code here
        if not grid or not grid[0]:
            return 0

        self.grid = grid
        self.visited = set()
        num_islands = 0

        width = len(grid[0])
        height = len(grid)

        for x in range(height):
            for y in range(width):
                if self.grid[x][y] and (x, y) not in self.visited:
                    self.visited.add((x, y))
                    self.bfs(x, y)
                    num_islands += 1
        return num_islands

    def bfs(self, x, y):
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        queue = deque([(x, y)])

        while queue:
            x, y = queue.popleft()
            for direction in range(len(dx)):
                newx = x + dx[direction]
                newy = y + dy[direction]
                if self.isvalid(newx, newy):
                    self.visited.add((newx, newy))
                    queue.append((newx, newy))

    def isvalid(self, x, y):
        return (0 <= x < len(self.grid)) and \
               (0 <= y < len(self.grid[0])) and \
               self.grid[x][y] and \
               (x, y) not in self.visited


