class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if len(nums) == 0 or (len(nums) == 1 and not nums[0] == target):
            return -1
        
        if len(nums) == 1 and nums[0] == target:
            return 0
        
        def binarySearch(left, right, nums, target):
            if right-left == 0:
                if nums[right] is not target:
                    return -1
                else:
                    return right

            middle_index = (right - left)//2 + left
            
            if nums[middle_index] == target:
                return middle_index
            
            elif nums[middle_index] > target:
                return binarySearch(left, middle_index, nums, target)
            elif nums[middle_index] < target:
                return binarySearch(middle_index+1, right, nums, target)

        index = binarySearch(0, len(nums)-1, nums, target)
        return index