class Solution:
    def rotateArray(self, nums, k: int) -> None:
        k = k%len(nums)
        newarray = nums[0:k]
        slicedarray = nums[k:]
        slicedarray.extend(newarray)
        nums[:] = slicedarray
        return nums
'''
now if k>len(nums):
        shift 8-len(nums)
        I slice nums into two arrays
        newarray = nums[0:k]
        slicedarray = nums[k+1:]
        return slicedarray.extend(newarray)
    else:
        shift k times
'''