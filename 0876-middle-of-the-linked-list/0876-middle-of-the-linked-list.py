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
         
        # print(head)
        # print(tail_node(head))
        print(length)
        print(length%2)
        cnt = head
        
        for _ in range(length//2) :
            cnt = cnt.next
        # else :
        #     for _ in range((length//2)):
        #         cnt = cnt.next
        # ans = []
        # while cnt.next != None :
        #     ans.append(cnt.val)
        #     cnt = cnt.next                
        return cnt