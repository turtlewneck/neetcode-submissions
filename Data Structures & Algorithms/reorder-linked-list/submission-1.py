# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''singly inked, so i guess two pointers
        ok before anything, how do i understand this problem?
        i have a list, and i need to move, starting from the last,
        every node in the style of 0, n-1, 1, n-2, 2, n-3, 3 etc
        so if i have an array like this 
        [1,2,3,4,5,6,7,8]
        it will look like this
        [1,8,2,7,3,6,4,5]
        I donkt know how long the list will be
        if i wanted to do this in a way of going to the almost end, change the pointer of the next
        (which is in reality the last one in the list) to the first one

        [1,2,3,4,5,6,7,8]
        i == 1, j == 7
        j.next == 8 -> j.next.next = i.next -> 8.next == 2
        i.next == 2 -> i.next = j.next -> 1.next == 8
        j.next == 8 -> j.next = None -> 7.next == None
        j is still at 7,
        i is still at 1,
        i = i.next.next
        j = i.next
        i == 2, j == 3
        ---- 3 times while
        i == 2, j == 6
        [1,8,2,3,4,5,6,7]
        i == 2, j == 6
        j.next == 7 -> j.next.next = i.next -> 7.next == 3
        i.next == 3 -> i.next = j.next -> 2.next == 7
        j.next == 7 -> j.next = None -> 6.next == None
        j is still at 6,
        i is still at 3,
        i = i.next.next
        j = i.next
        i == 3, j == 4
        ---- 1 time while
        i == 3, j == 5

        [1,8,2,7,3,4,5,6]
        i == 3, j == 5
        j.next == 6 -> j.next.next = i.next -> 6.next == 4
        i.next == 4 -> i.next = j.next -> 3.next == 6
        j.next == 6 -> j.next = None -> 5.next == None
        j is still at 5,
        i is still at 3,
        i = i.next.next
        j = i.next
        i == 4, j == 5
        ---- 1 time while
        i == 3, j == 5
        [1,8,2,7,3,6,4,5] end
        pointer i at the [0], pointer j at the [1]
        pointer j moves to the almost very end (check the next.next == none)
        then change [j.next.next] to i.next,
        then change i.next to j.next, 
        then change j.next to None
        repeat until?
        until i < j? i <= j?
        O(N^2), because iterating over the whole array once and then 1/2n, which is still n
        '''
        #check if two or less
        if head == None:
            return
        elif head.next == None:
            return
        elif head.next.next == None:
            return

        i = j = head
        while j != None and j.next != None:

            if j.next.next == None:
                j.next.next = i.next
                i.next = j.next
                j.next = None

                i = i.next.next
                j = i.next
            else:
                j = j.next
        
        return
        

