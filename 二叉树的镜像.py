# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root:
            root.right,root.left=root.left,root.right
            self.Mirror(root.left)
            self.Mirror(root.right)
        else:
            return