class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first check the middle index of row and first element
        # if lower  -> previous row, last element?
        # if higher -> last element? or first of next row? i guess last element
        # if hit    -> return index
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1

        #def bsearch(l, r, t, b):

        # what if i did it iteratively?
        # what would that look like?
        while top <= bottom:
            # check for the row
            midv = (top + bottom) // 2
            if matrix[midv][left] > target: # previous rows
                bottom = midv - 1
            elif matrix[midv][right] < target: # next rows
                top = midv + 1
            else: # this row
                while left <= right:
                    midh = (left + right) // 2
                    val = matrix[midv][midh]
                    if val == target:
                        return True
                    elif val > target:
                        right = midh - 1
                    else:
                        left = midh + 1
        return False
