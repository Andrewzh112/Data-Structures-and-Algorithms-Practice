# Letter Combinations of a Phone Number
class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    def letterCombinations(self, digits):
        # write your code here
        self.keys = {
                     '2': 'abc',
                     '3': 'def',
                     '4': 'ghi',
                     '5': 'jkl',
                     '6': 'mno',
                     '7': 'pqrs',
                     '8': 'tuv',
                     '9': 'wxyz'
                }
        if not digits:
            return []

        results = []
        self.dfs(digits, 0, [], results)
        return results
    
    def dfs(self, digits, startIndex, combo, results):
        if len(digits) == startIndex:
            results.append(''.join(combo))
            return
        for letter in self.keys[digits[startIndex]]:
            print(digits[startIndex], digits)
            combo.append(letter)
            self.dfs(digits, startIndex + 1, combo, results)
            combo.pop()


# Next Permutation
class Solution1:
    """
    @param nums: A list of integers
    @return: A list of integers
    """
    def nextPermutation(self, nums):
        # write your code here
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                break
        else:
            nums.reverse()
            return nums
        for j in range(len(nums)-1, i, -1):
            if nums[j] > nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                break
        for j in range(0, (len(nums) - i)//2):
            nums[i+j+1], nums[len(nums)-j-1] = nums[len(nums)-j-1], nums[i+j+1]
        return nums


# Word Search II
class Solution2:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        if board is None or board[0] is None or len(board) == 0 or len(board[0]) == 0:
            return []
        m = len(board)
        n = len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        prefixset = self.getprefix(words)
        wordset = []
        for i in range(m):
            for j in range(len(board[i])):
                visited[i][j] = True
                self.dfs(board, visited, i, j, board[i][j], prefixset, wordset)
                visited[i][j] = False
        return wordset
    
    def getprefix(self, words):
        prefixset = {}
        for word in words:
            for i in range(len(word) - 1):
                prefix = word[0: i + 1]
                if prefix not in prefixset:
                    prefixset[prefix] = False
            prefixset[word] = True
        return prefixset
    
    def dfs(self, board, visited, x, y, word, prefixset, wordset):
        if word not in prefixset:
            return
        if prefixset.get(word) and word not in wordset:
            wordset.append(word)
        dx = [1, 0, 0, -1]
        dy = [0, 1, -1, 0]
        for i in range(len(dx)):
            adjx = x + dx[i]
            adjy = y + dy[i]
            if (not self.insideboard(board, adjx, adjy)) or (visited[adjx][adjy]):
                continue
            visited[adjx][adjy] = True
            self.dfs(board, visited, adjx, adjy, word + board[adjx][adjy], prefixset, wordset)
            visited[adjx][adjy] = False
    
    def insideboard(self, board, x, y):
        return x >= 0 and x < len(board) and y >= 0 and y < len(board[0])
