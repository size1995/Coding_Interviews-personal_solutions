# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if not (pRoot1 and pRoot2):
            return False
        return self.hassub(pRoot1, pRoot2) or self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right,pRoot2)
    def hassub(self, A, B):
        if not B:
            return True
        if A == None or A.val != B.val:
            return False
        return self.hassub(A.left, B.left) and self.hassub(A.right, B.right)
