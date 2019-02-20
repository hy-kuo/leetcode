# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: 'ListNode', n: 'int') -> 'ListNode':
        first = head
        second = None
        cnt = 0
        while first!=None:
            first = first.next
            cnt += 1
            if cnt == n+1:
                second = head
            elif cnt > n:
                second = second.next
        del_node = None
        if second:
           del_node = second.next
        else:
            del_node = head
        if del_node!=head:
            second.next = del_node.next
        else:
            head = head.next
        del del_node
        return head
            
        