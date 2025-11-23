# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cnt = head
        length = 1
        while cnt.next != None :
            cnt = cnt.next
            length += 1
        
        cnt = head
        
        for _ in range(length//2) :
            cnt = cnt.next
                   
        return cnt