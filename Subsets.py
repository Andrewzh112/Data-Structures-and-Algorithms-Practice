class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self,nums):
        # write your code here
        results=[]
        if not nums:
            return [results]
        nums.sort()
        self.dfs(0,nums,[],results)
        return results
    
    def dfs(self,start_index,nums,subset,results):
        results.append(list(subset))
        
        for i in range(start_index,len(nums)):
            subset.append(nums[i])
            self.dfs(i+1,nums,subset,results)
            subset.pop()