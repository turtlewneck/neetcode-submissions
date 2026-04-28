/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode tmp, bgn = new ListNode();
        tmp = bgn;

        //check which is smaller, then append
        //5,7   1,2,3,4,8
        while(true) {
            if (list1 == null && list2 == null){
                break;
            }
            else if(list1 == null) {
                bgn.next = list2;
                bgn = bgn.next;
                list2 = list2.next;
            }
            else if(list2 == null) {
                bgn.next = list1;
                bgn = bgn.next;
                list1 = list1.next;
            }
            else if (list1.val < list2.val) {
                bgn.next = list1;
                bgn = bgn.next;
                list1 = list1.next;
            } else {
                bgn.next = list2;
                bgn = bgn.next;
                list2 = list2.next;
            }
        }
        return tmp.next;
    }
}