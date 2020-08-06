# two sum unique pairs
class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        start, end = 0, len(nums) - 1
        nums.sort()
        pairs = 0
        while start < end:
            if start > 0 and nums[start] == nums[start - 1]:
                start += 1
            elif end < len(nums) - 1 and nums[end] == nums[end + 1]:
                end -= 1
            elif nums[start] + nums[end] == target:
                pairs += 1
                start += 1
                end -= 1
            elif nums[start] + nums[end] < target:
                start += 1
            else:
                end -= 1
        return pairs


# 3sum
class Solution2:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        numbers.sort()
        answers = []
        for i in range(len(numbers) - 1, 1, -1):
            if i < len(numbers) - 1 and numbers[i] == numbers[i + 1]:
                continue
            two_sums = self.twoSum(numbers[:i], 0 - numbers[i])
            for two_sum in two_sums:
                two_sum.extend([numbers[i]])
                answers.append(two_sum)
        return answers
        
    def twoSum(self, numbers, target):
        two_sums = []
        start, end = 0, len(numbers) - 1
        print(numbers)
        while start < end:
            if end < len(numbers) - 1 and numbers[end] == numbers[end + 1]:
                end -= 1
            elif start > 0 and numbers[start] == numbers[start - 1]:
                start += 1
            elif numbers[start] + numbers[end] == target:
                two_sums.append([numbers[start], numbers[end]])
                start += 1
                end -= 1
            elif numbers[start] + numbers[end] < target:
                start += 1
            else:
                end -= 1
        return two_sums


# Triangle Count
class Solution3:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        # write your code here
        S.sort()
        triangle_counts = 0
        for i in range(len(S) - 1, 1, -1):
            bigger_sums = self.bigger_sum(S[:i], S[i])
            triangle_counts +=  bigger_sums
        return triangle_counts
    
    def bigger_sum(self, nums, target):
        left, right = 0, len(nums) - 1
        bigger_sums = 0
        while left < right:
            if nums[left] + nums[right] <= target:
                left += 1
            else:
                bigger_sums += right - left
                right -= 1
        return bigger_sums


# Partition Array
class Solution4:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        left, right = 0, len(nums) - 1
        while left <= right:
            while left <= right and nums[left] < k:
                left += 1
            while left <= right and nums[right] >= k:
                right -= 1
            if left <= right:
                nums[right], nums[left] = nums[left], nums[right]
                right -= 1
                left += 1
        return left


# Kth Smallest Numbers in Unsorted Array
class Solution5:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    def kthSmallest(self, k, nums):
        # write your code here
        return self.quick_select(0, len(nums) - 1, nums, k - 1)
    
    def quick_select(self, start, end, nums, k):
        if start == end:
            return nums[start]
        pivot = nums[(start + end) // 2]
        left, right = start, end
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        if right >= k and start <= right:
            return self.quick_select(start, right, nums, k)
        if left <= k and left <= end:
            return self.quick_select(left, end, nums, k)
        return nums[k]
