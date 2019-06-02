# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def __init__(self):
        self.node=[]
    def FindKthToTail(self, head, k):
        if head==None:
            return None
        while head:
            self.node.append(head)
            head=head.next
        if k>len(self.node) or k<=0:
            return None
        else:
            return self.node[len(self.node)-k]
