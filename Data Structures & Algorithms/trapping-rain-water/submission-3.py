class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = height[0]
        maxR = height[-1]
        l = res = 0
        r = len(height) - 1

        while l<r:
            if maxL <= maxR:
                h = maxL - height[l]
                if h > 0:
                    res += h
                l+=1
                maxL = max(maxL, height[l])
            else:
                h = maxR - height[r]
                if h > 0:
                    res += h
                r-=1
                maxR = max(maxR, height[r])

        return res
        
        # ok i think i know how to solve this
        # two pointers from the beginning, calc min, if not zero and if diff index > 1 (not next to
        # each other) calct diff index * min, if i min -> i++, if j min -> there wont be anything 
        # higher to the left, so point it to the i and increment the i
        # i = 1
        # j = res = 0
        # while i < len(height):
        #     curr = min(height[i], height[j])
        #     if curr and i - j > 1:
        #         res += (i-j-1)*curr
        # different approach, as he explained in the video
        # i have to determine if the place is valid, so if the height of current index has 
        # left higher partner and right higher partner, what, is valid? yee array with 
        # res = 0
        # pref = [0]*len(height)
        # #post = [0]*len(height)
        # # can be an array of suffixes and then the array of prefixes or the other way around
        # maximum = 0
        # for i in range(1,len(height)):
        #     pref[i] = maximum = max(maximum, height[i-1])
        
        # maximum = 0
        # # for i in range(len(height) - 2, -1, -1):
        # for i in range(len(height) - 2, 0, -1):
        #     # post[i] = maximum = max(maximum, height[i+1])
        #     curr = maximum = max(maximum, height[i+1])
        #     h = min(pref[i], curr)-height[i]
        #     if h > 0:
        #         res+=h
        # return res
        # # for i in range(len(height)):
        # #     h = min(pref[i], post[i]) - height[i]
        # #     if h > 0:
        # #         res+=h
        # # return res