# Sort Colors
class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        start = i = 0
        end = len(nums) - 1
        
        while i <= end:
            if nums[i] == 0:
                nums[i], nums[start] = nums[start], nums[i]
                i += 1
                start += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[end] = nums[end], nums[i]
                end -= 1


# Sort ColorsII
class Solution1:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        self.sort(colors, 0, len(colors) - 1, 1, k)

    def sort(self, colors, start, end, colorFrom, colorTo):
        if start >= end or colorFrom == colorTo:
            return
        colorMid = colorFrom + (colorTo - colorFrom) // 2
        left, right = start, end
        while left <= right:
            while left <= right and colors[left] <= colorMid:
                left += 1
            while left <= right and colors[right] > colorMid:
                right -= 1
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]

        self.sort(colors, start, right, colorFrom, colorMid)
        self.sort(colors, left, end, colorMid + 1, colorTo)


# Move Zeros
class Solution2:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        left, right = 0, 0
        while right < len(nums):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
            right += 1