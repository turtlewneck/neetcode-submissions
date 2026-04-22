class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1] or len(nums) == 1: # check if was rotated
            return nums[0] # not rotated
        # has been rotated
        # binary search?
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r)//2
            val = nums[mid]
            if val > nums[mid + 1]: #the smallest is mid+1
                return nums[mid + 1]
            if val < nums[mid + 1] and val < nums[-1]: # np 3, 4 <- move right pointer 
                r = mid
            elif val < nums[mid + 1] and val > nums[-1]:
                l = mid