# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return
        self.Convert(pRootOfTree.left)
        left=pRootOfTree.left
        if left:
            while left.right:
                left=left.right
            left.right=pRootOfTree
            pRootOfTree.left=left
        self.Convert(pRootOfTree.right)
        right=pRootOfTree.right
        if right:
            while right.left:
                right=right.left
            right.left=pRootOfTree
            pRootOfTree.right=right
        while pRootOfTree.left:
            pRootOfTree=pRootOfTree.left
        return pRootOfTree
