#Remove Nth Node From End of List:https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#Solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next == None:
            return []
        d = head
        e = head
        b = head
        i = 0
        while e.next != None:
            e = e.next
            i = i+1
            if i >= n:
                d = d.next
                if i>n:
                    b = b.next
            #print(l.val)
            #print(p.val)
        if b == head and b == d:
            head = head.next
        else:
            b.next = d.next
            d.next = None
        return head