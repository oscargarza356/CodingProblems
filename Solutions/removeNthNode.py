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
        dummyNode =  head
        count = 0
        while dummyNode:
            dummyNode = dummyNode.next
            count += 1
            
        end = abs(count - n) 
        count= 1
        print("end",end)
        if end == 0:
            return head.next
        beg= head
        while True:
            if count == end:
                print("head",head.val)
                dummyNode = head.next
                head.next = dummyNode.next 
                break
            head = head.next
            count += 1
        
        return beg
