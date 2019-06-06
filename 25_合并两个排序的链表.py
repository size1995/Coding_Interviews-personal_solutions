# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def Merge(self, pHead1, pHead2):
        s=ListNode(0)
        p=s
        while pHead1 and pHead2:
            if pHead1.val>pHead2.val:
                s.next=pHead2
                pHead2=pHead2.next
            else:
                s.next=pHead1
                pHead1 = pHead1.next
            s=s.next
        if pHead1:
            s.next=pHead1
        else:
            s.next=pHead2
        return p.next
