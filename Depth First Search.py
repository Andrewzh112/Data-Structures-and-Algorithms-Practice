# Subset
class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        # write your code here
        nums.sort()
        results = []
        self.dfs(nums, [], results, 0)
        return results
    
    def dfs(self, nums, subset, results, startIndex):
        results.append(list(subset))
        
        for i in range(startIndex, len(nums)):
            subset.append(nums[i])
            self.dfs(nums, subset, results, i + 1)
            subset.pop()


# Subset II
class Solution2:
    """
    @param nums: A set of numbers.
    @return: A list of lists. All valid subsets.
    """
    def subsetsWithDup(self, nums):
        # write your code here
        nums.sort()
        results = []
        self.dfs(0, [], results, nums)
        return results
        
    def dfs(self, startIndex, subset, results, nums):
        results.append(list(subset))
        
        for i in range(startIndex, len(nums)):
            if i > startIndex and nums[i] == nums[i - 1]:
                continue
            subset.append(nums[i])
            self.dfs(i + 1, subset, results, nums)
            subset.pop()


# permutation
class Solution3:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        seen = set()
        nums.sort()
        results = []
        self.dfs(nums, results, [], seen)
        return results
    def dfs(self, nums, results, permutation, seen):
        if len(nums) == len(permutation):
            results.append(list(permutation))
            return
        for i in range(len(nums)):
            if nums[i] in seen:
                continue
            seen.add(nums[i])
            permutation.append(nums[i])
            self.dfs(nums, results, permutation, seen)
            seen.remove(nums[i])
            permutation.pop()


# Permutation II
class Solution4:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        nums.sort()
        seen = [False] * len(nums)
        result = []
        self.dfs(nums, [], result, seen)
        return result
        
    def dfs(self, nums, permutation, result, seen):
        if len(nums) == len(permutation):
            result.append(list(permutation))
            return
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i -1] and not seen[i - 1]:
                continue
            if seen[i]:
                continue
            seen[i] = True
            permutation.append(nums[i])
            self.dfs(nums, permutation, result, seen)
            seen[i] = False
            permutation.pop()


# Combination Sum
class Solution5:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        results = []
        candidatesNew = sorted(list(set(candidates)))
        self.dfs(0, results, [], candidatesNew, target)
        return results
    def dfs(self, startIndex, results, subset, candidates, target):
        if target == 0:
            results.append(list(subset))
            return
        for i in range(startIndex, len(candidates)):
            if target < candidates[i]:
                break
            subset.append(candidates[i])
            self.dfs(i, results, subset, candidates, target - candidates[i])
            subset.pop()
