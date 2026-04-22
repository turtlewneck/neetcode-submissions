class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search =>
        # take mid index, look if is the target
        # if yes => return mid
        # else if lower => search again with mid as lower index
        # else if higher => search again as mid as higher index
        # if lower index = higher index  => 
        # if nums[index] != target => return -1
        # if nums[index] = target +> return index
        
        #----------------RECURSIVE-------------
        # def bsearch(l, r):
        #     if l > r:
        #         return -1
        #     if l == r:
        #         if nums[l] == target:
        #             return l
        #         else:
        #             return -1
        #     mid = (l + r) // 2
        #     val = nums[mid]
        #     if val == target:
        #         return mid
        #     elif val > target:
        #         return bsearch(l, mid - 1)
        #     else:
        #         return bsearch(mid + 1, r)
        
        # res = bsearch(0, len(nums)-1)
        # return res

        #----------------ITERATIVE
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            val = nums[mid]
            if val == target:
                return mid
            elif val > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1