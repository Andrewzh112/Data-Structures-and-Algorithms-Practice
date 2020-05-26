class Solution:
    """
    @param candidates: A list of integers
    @param target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, candidates, target):
        # write your code here
        results = []
        
        if not candidates:
            return [candidates]
            
        candidates.sort()
        nums = self.remove_duplicates(candidates)
        
        self.dfs(nums,0,[],results,target)
        return results
        
        
    def remove_duplicates(self, candidates):
        nums = []
        
        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i-1]:
                continue
            nums.append(candidates[i])
        return nums
       
        
    def dfs(self, nums, startIndex, subset, results, target):
        if target < 0:
            return
        
        if target == 0:
            results.append(list(subset))
            return
        
        for i in range(startIndex, len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            subset.append(nums[i])
            self.dfs(nums,i,subset,results,target-nums[i])
            subset.pop()