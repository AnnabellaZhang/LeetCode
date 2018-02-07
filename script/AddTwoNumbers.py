#Add Two Numbers: https://leetcode.com/problems/add-two-numbers/description/
# Submission: 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        Iso = 0
        head = ListNode(None)
        l3 = head
        while l1!=None and l2!=None:
            l3.next = ListNode(l1.val+l2.val+Iso if l1.val+l2.val+Iso<10 else l1.val+l2.val+Iso-10)
            Iso = 1 if l1.val+l2.val+Iso >9 else 0
            l1 = l1.next
            l2 = l2.next
            l3 = l3.next
        if l1 == None and l2 != None:
            while l2 != None:
                l3.next = ListNode(l2.val+Iso if l2.val+Iso<10 else l2.val+Iso-10)
                Iso = 1 if l2.val+Iso >9 else 0
                l2 = l2.next
                l3 = l3.next
        if l1 != None and l2 == None:
            while l1 != None:
                l3.next = ListNode(l1.val+Iso if l1.val+Iso<10 else l1.val+Iso-10)
                Iso = 1 if l1.val+Iso >9 else 0
                l1 = l1.next
                l3 = l3.next
        if Iso != 0:
            l3.next = ListNode(Iso)
        return head.next