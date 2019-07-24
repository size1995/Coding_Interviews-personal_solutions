# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if pHead==None:
            return pHead
        current_node=pHead
        while (current_node!=None):
            next_node=current_node.next
            tempt_node=RandomListNode(current_node.label)
            tempt_node.next=next_node
            current_node.next=tempt_node
            current_node=next_node
        current_node=pHead
        while(current_node!=None):
            if current_node.random==None:
                current_node.next.random=None
            else:
                current_node.next.random=current_node.random.next
            current_node=current_node.next.next
        current_node=pHead
        p_clone_head=pHead.next
        while(current_node!=None):
            clone_node=current_node.next
            current_node.next=clone_node.next
            if clone_node.next==None:
                clone_node.next=None
            else:
                clone_node.next=clone_node.next.next
            current_node=current_node.next
        return p_clone_head
        # write code here