class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        if not A:
            return -1
        start,end=0,len(A)-1
        min_index=self.get_min(A)
        if target<=A[end]:
            return self.binary_search(min_index,end,A,target)
        return self.binary_search(start,min_index-1,A,target)
        
    def binary_search(self,start,end,A,target):
        while start+1<end:
            mid=start+(end-start)//2
            if A[mid]<=target:
                start=mid
            else:
                end=mid
        
        if A[start]==target:
            return start
        if A[end]==target:
            return end
        return -1
        
    def get_min(self,A):
        start,end=0,len(A)-1
        while start+1<end:
            mid=start+(end-start)//2
            if A[mid]>A[end]:
                start=mid
            else:
                end=mid
        
        if A[start]<=A[end]:
            return start
        return end