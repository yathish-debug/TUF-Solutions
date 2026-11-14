class Solution:
    def secondLargestElement(self, nums):
        last = float('-inf')
        sec_last = float('-inf')
        for i in range(len(nums)):
            if nums[i]<=last:
                if nums[i]>=sec_last and nums[i]!=last:
                    sec_last = nums[i]
                else:
                    continue
            else:
                    sec_last = last
                    last =  nums[i]
        return sec_last if sec_last!=float('-inf') else -1

'''
maintain 2 pointers, last & sec_last
loop through nums, as soon as you find a number<= last 
'''