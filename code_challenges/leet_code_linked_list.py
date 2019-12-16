# Add Two Numbers

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        head = l3 = ListNode(0)
        carry = 0
        
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val 
                l2 = l2.next
                
            l3.val = carry % 10
            carry = carry // 10
            
            if l1 or l2 or carry:
                l3.next = ListNode(0)
                l3 = l3.next
                
        return head

###########################################################

# Merge Two Linked Lists

# # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p = l1
        q = l2
        s = None
    
        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.val <= q.val:
                s = p 
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s 
        while p and q:
            if p.val <= q.val:
                s.next = p 
                s = p 
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q 
        if not q:
            s.next = p 

        return new_head

###########################################################

# Remove Duplicates from Linked Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if not head:
            return
        
        cur = head.next
        start = head
        prev = head
        
        while cur:
            if cur.val == prev.val:
                prev.next = cur.next
            else:
                prev = cur      
                
            cur = cur.next
            
        return start


###########################################################

# Reverse a Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        current = head
        prev = None
        
        while current:
            nxt = current.next
            current.next = prev

            prev = current
            current = nxt

        head = prev
        
        return head