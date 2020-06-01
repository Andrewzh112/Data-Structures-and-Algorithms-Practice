class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        # write your code here
        results = []
        
        if not nums:
            return [results]
            
        nums.sort()
        self.dfs(nums, [False] * len(nums), [], results)
        return results
        
        
    def dfs(self, nums, seen, permutations, results):
        if len(nums) == len(permutations):
            results.append(list(permutations))
        
        for i in range(len(nums)):
            
            if i > 0 and nums[i] == nums[i -1] and not seen[i - 1]:
                continue
                
            if seen[i]:
                continue

            permutations.append(nums[i])
            seen[i] = True
            self.dfs(nums, seen, permutations, results)
            seen[i] = False
            permutations.pop()