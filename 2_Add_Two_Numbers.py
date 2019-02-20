# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: 'ListNode', l2: 'ListNode') -> 'ListNode':
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        p1 = l1
        p2 = l2
        carry = 0
        head, carry = ListNode((p1.val + p2.val + carry)%10), int((p1.val + p2.val + carry)/10) 
        
        p1 = p1.next
        p2 = p2.next
        p = head
        while p1 or p2:
            if p1 and p2:
                p.next, carry =  ListNode((p1.val + p2.val + carry)%10), int((p1.val + p2.val + carry)/10) 
                p1, p2 = p1.next, p2.next
            elif p1 == None:
                p.next, carry =  ListNode((p2.val + carry)%10), int((p2.val + carry)/10)
                p2 = p2.next
            elif p2 == None:
                p.next, carry =  ListNode((p1.val + carry)%10), int((p1.val + carry)/10) 
                p1 = p1.next
            p = p.next
        if carry:
            p.next = ListNode(carry)
        return head
        