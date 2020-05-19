class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        results=[]
        if not nums:
            return [results]
        
        seen=[False]*len(nums)
        self.dfs(nums,seen,[],results)
        return results
        
        
    def dfs(self,nums,seen,combination,results):
        if len(combination)==len(nums):
            results.append(list(combination))
            return
        for i in range(len(nums)):
            if seen[i]:
                continue
            
            seen[i]=True
            combination.append(nums[i])
            self.dfs(nums,seen,combination,results)
            seen[i]=False
            combination.pop()