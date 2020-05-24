class Solution:
    """
    @param n: An integer
    @param nums: An array
    @return: the Kth largest element
    """
    def kthLargestElement(self, n, nums):
        # write your code here
        if not nums or n < 1 or n > len(nums):
            return None
            
        start, end = 0, len(nums) - 1
        return self.quick_sort(start, end, len(nums) - n, nums)
        
        
    def quick_sort(self, start, end, k, nums):
        if start == end:
            return nums[k]
        
        left, right = start, end
        pivot = nums[start + (end- start) // 2]
        
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
                
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        if k <= right:
            return self.quick_sort(start,right,k,nums)
        if k >=left:
            return self.quick_sort(left,end,k,nums)
        return nums[k]