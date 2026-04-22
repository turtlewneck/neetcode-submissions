class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nm = dict()
        smallest = sys.maxsize
        for i, n in enumerate(nums):
            if n <= 0:
                continue
            nm[n] = i
        if 1 not in nm:
            return 1
        smallest = min(nm)
        for i in nm.keys():
            if smallest-1 not in nm and smallest != 1:
                return smallest-1
            elif smallest+1 not in nm:
                return smallest+1
            elif smallest+1 in nm:
                smallest = smallest+1