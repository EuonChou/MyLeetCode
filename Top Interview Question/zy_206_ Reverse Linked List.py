# Reverse a singly linked list.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        pre, p = None, head

        while p:
        	tail = p.next
        	p.next = pre
        	pre = p
        	p = tail


        return pre




#     def reverseList(self, head):
		#递归写法
#     	if head==None or head.next==None:
#     		return head

#     	p = self.reverseList(head.next)
#     	head.next.next = head
#     	head.next = None
#     	return p

