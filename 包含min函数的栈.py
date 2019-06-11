# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stak=[]
        self.min_stak=[]
    def push(self,node):
        if not self.min_stak or node<self.min_stak[-1]:
            self.min_stak.append(node)
        else:
            self.min_stak.append(self.min_stak[-1])
        self.stak.append(node)
    def pop(self):
        if len(self.stak)==0:
            return None
        self.min_stak.pop()
        return self.stak.pop()
    def top(self):
        if len(self.stak)==0:
            return None
        return self.stak[-1]
    def min(self):
        return self.min_stak[-1]