# -*- coding:utf-8 -*-
class Solution:
    def printMatrix(self, matrix):
        out_list=[]
        while matrix:
            out_list+=matrix.pop(0)
            matrix = list(zip(*matrix))
            for i in range(len(matrix)):
                matrix[i] = list(matrix[i])
            matrix=matrix[::-1]
        return out_list