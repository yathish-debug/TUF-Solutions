class Solution:
    def largestElement(self, nums):
        largest_num = float('-inf')
        for i in range(len(nums)):
            if nums[i]>largest_num:
                largest_num = nums[i]
        return largest_num
        