# Two Sum (sorted)
class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, nums, target):
        # write your code here
        start, end = 0, len(nums) - 1
        
        while start <= end:
            if nums[start] + nums[end] == target:
                return [start + 1, end + 1]
                
            if nums[start] + nums[end] > target:
                end -= 1
            else:
                start += 1


# Quick Sort
class Solution1:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        self.quick_sort(0, len(A) - 1, A)
        return A
    
    
    def quick_sort(self, start, end, A):
        if start >= end:
            return
        
        left, right = start, end
        pivot = A[(start + end) // 2]
        
        while left <= right:
            while left <= end and A[left] < pivot:
                left += 1
            while right >= start and A[right] > pivot:
                right -= 1
                
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1
                right -= 1
        self.quick_sort(start, right, A)
        self.quick_sort(left, end, A)


# Merge Sort
class Solution2:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # write your code here
        temp = [None for _ in range(len(A))]
        return self.merge_sort(0, len(A) - 1, A, temp)
        
    def merge_sort(self, start, end, A, temp):
        if start >= end:
            return
        
        mid = (start + end) // 2
        self.merge_sort(start, mid, A, temp)
        self.merge_sort(mid + 1, end, A, temp)
        
        self.merge(start, mid, end, A, temp)
        
    def merge(self, start, mid, end, A, temp):
        left, right = start, mid + 1
        index = start
        
        while left <= mid and right <= end:
            if A[left] <= A[right]:
                temp[index] = A[left]
                left += 1
            else:
                temp[index] = A[right]
                right += 1
            index += 1
        
        while left <= mid:
            temp[index] = A[left]
            left += 1
            index += 1
        
        while right <= end:
            temp[index] = A[right]
            right += 1
            index += 1
            
        for i in range(start, end + 1):
            A[i] = temp[i]