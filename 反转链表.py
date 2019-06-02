# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        if not pHead:
            return None
        if pHead.next==None:
            return pHead
        now =None
        while pHead:
            now1 = ListNode(pHead.val)
            now1.next = now
            now=now1
            pHead=pHead.next
        return now
