class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count=0
        maxi = -1
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
                maxi = max(maxi, count)
                print(count)
            else:
                count=0
                print(count)
        return maxi if maxi!=-1 else 0

        