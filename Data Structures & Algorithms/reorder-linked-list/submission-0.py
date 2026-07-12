# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head):
        prev = None 
        curr = head 

        while curr:
            nxt = curr.next 
            curr.next = prev 
            prev = curr
            curr = nxt 

        return prev 

    def listLen(self, head):
        lenn = 0 
        while head:
            lenn += 1 
            head = head.next 

        return lenn 
        
    def reorderList(self, head: Optional[ListNode]) -> None:
        lenn = self.listLen(head) 

        breakPoint = math.ceil(lenn / 2) 

        ind = 0 
        curr = head 
        while ind < breakPoint - 1:
            ind += 1 
            curr = curr.next
        
        
        secondHead = curr.next 
        curr.next = None 

        secondHead = self.reverseList(secondHead) 
        firstHead = head 
    
        while firstHead and secondHead:
            temp1 = firstHead.next
            temp2 = secondHead.next

            firstHead.next = secondHead
            secondHead.next = temp1

            firstHead = temp1
            secondHead = temp2