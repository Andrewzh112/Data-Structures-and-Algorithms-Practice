# Classic Binary Search
class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        if not nums:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] == target:
                end = mid
            elif nums[mid] < target:
                start = mid
            else:
                end = mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1


# Search in a Big Sorted Array
class Solution2:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        start, end = 0, 1
        while reader.get(end) < target:
            end *= 2
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if reader.get(mid) == target:
                end = mid
            elif reader.get(mid) < target:
                start = mid
            else:
                end = mid
        
        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        return -1


# Find K Closest Elements
class Solution3:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        lower, upper = self.get_bounds(A, target)
        results = []
        while len(results) < k:
            if abs(target-A[lower]) <= abs(target-A[upper]):
                results.append(A[lower])
                lower -= 1
                if lower < 0:
                    nmore = k - len(results)
                    for _ in range(nmore):
                        results.append(A[upper])
                        upper += 1
                    break
            else:
                results.append(A[upper])
                upper += 1
                if upper == len(A):
                    nmore = k - len(results)
                    for _ in range(nmore):
                        results.append(A[lower])
                        lower -= 1
                    break
        return results
    
    
    def get_bounds(self, A, target):
        start, end = 0, len(A) - 1
        results = []
        while start + 1 < end:
            mid = start + (end - start) // 2
            if A[mid] < target:
                start = mid
            else:
                end = mid
        if start - 1 >= 0 and abs(target-A[start - 1]) < abs(target-A[start]):
            return start - 1, start
        if end + 1 < len(A) and abs(target-A[end + 1]) < abs(target-A[end]):
            return end, end + 1
        return start, end


# Maximum Number in Mountain Sequence
class Solution4:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # write your code here
        start, end = 0, len(nums) - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[mid + 1]:
                end = mid
            else:
                start = mid
        return max(nums[start], nums[end])


# Find Minimum in Rotated Sorted Array
class Solution5:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        start, end = 0, len(nums) - 1
        if nums[start] < nums[end]:
            return nums[start]
        while start + 1 < end:
            mid = start + (end - start) // 2
            if nums[start] > nums[mid]:
                end = mid
            else:
                start = mid
        return min(nums[start], nums[end])


# Find Peak Element
class Solution6:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        start, end = 0, len(A) - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            
            if A[mid] > A[mid + 1] and A[mid] > A[mid -1]:
                return mid
            if A[mid + 1] < A[mid]:
                end = mid
            else:
                start = mid
        if A[start] >= A[end]:
            return start
        return end


# 
