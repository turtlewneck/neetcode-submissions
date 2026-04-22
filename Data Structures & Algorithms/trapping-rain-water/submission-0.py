class Solution:
    def trap(self, height: List[int]) -> int:
        # ok what i thought would be a way to solve this question is to find every
        # pair of rows that are between walls, but it would be at least O(n^2), because i would
        # have to two pointer every row, but the expected time is O(n), therefore i have to come
        # up with something smarter. For now, this is still a valid solution

        maxHeight = max(height)
        res = 0
        for row in range(maxHeight): # loop 0->3
            i = 1
            j = 0
            while i < len(height):
                # here checking if we have a wall, if we do -> determine if j is also a wall,
                # if not, then point j to i, and search for next wall with i

                if height[i] - row > 0:
                    #is higher, so this is a wall
                    #check if j is also a wall, if not -> point j to i, and i+=1, and 
                    # if is - calculate the difference between them and add to res AND
                    # i have to decrement it, bc if walls next to each other -> no water yet 1
                    if height[j] - row > 0:
                        res += i-j - 1
                    # whether or not j was a wall, now it has to be apppointed to i
                    j = i
                    i += 1
                
                # if i is not a wall, we simply iterate again 
                else:
                    i += 1
                #hope this works
        return res