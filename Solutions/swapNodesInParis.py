# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        currentNode = head
        switch = 0
        flag = True
        pastEven = None
        while currentNode:
            if switch:
                print (currentNode.val, pastNode.val)
                if flag == True:
                    head = currentNode
                    flag = False
                test = currentNode.next
                currentNode.next = pastNode
                pastNode.next = test
                if pastEven == None:
                    pastEven = pastNode
                    currentNode = pastNode.next
                    switch = 0   
                    continue
                pastEven.next = currentNode
                pastEven = pastNode
                currentNode = pastNode.next
                switch = 0   
                continue
            pastNode = currentNode
            currentNode = currentNode.next
            switch = 1
        
        return head
