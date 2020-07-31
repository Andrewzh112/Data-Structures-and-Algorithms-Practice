# Wood Cut
class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        if sum(L) < k:
            return 0
        start, end = 1, max(L)
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.num_logs(L, mid) < k:
                end = mid
            else:
                start = mid
        if self.num_logs(L, end) < k:
            return start
        return end
    def num_logs(self, L, length):
        return sum([l // length for l in L])


# Search a 2D Matrix
class Solution2:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        if matrix == None or len(matrix) == 0:
            return False
        n, m = len(matrix), len(matrix[0])
        x, y = 0, m-1
        while x <= n-1 and y >= 0:
            goal = matrix[x][y]
            if target > goal:
                x += 1
            if target < goal:
                y -= 1
            if target == goal:
                return True
        return False
