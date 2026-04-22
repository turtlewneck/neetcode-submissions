class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sNums = sorted(nums)
        res = []

        for i in range(len(sNums)):
            if sNums[i] > 0:
                break
            if i > 0 and sNums[i] == sNums[i - 1]:
                continue
            l = i + 1
            r = len(sNums)-1

            while l < r:
                total = sNums[l]+sNums[r]+sNums[i]
                if total == 0:
                    res.append([sNums[l],sNums[i],sNums[r]])
                    l += 1
                    r -= 1
                    while l < r and sNums[l] == sNums[l - 1]:
                        l += 1
                    while l < r and sNums[r] == sNums[r + 1]:
                        r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
        return res