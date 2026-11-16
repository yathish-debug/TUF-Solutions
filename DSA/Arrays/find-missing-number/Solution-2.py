class Solution:
    def missingNumber(self, nums):
        sum_nnumbers = len(nums)*(len(nums)+1)//2
        for i in nums:
            sum_nnumbers-=i
        return sum_nnumbers
        