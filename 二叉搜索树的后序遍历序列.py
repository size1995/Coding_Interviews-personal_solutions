class Solution:
    def VerifySquenceOfBST(self, sequence):
        if not sequence:return False
        if len(sequence) == 1: return True
        root = sequence.pop()
        left=[]
        for i in range(len(sequence)):
            if sequence[i] > root:break
            left.append(sequence[i])
        if len(left)==len(sequence):right=[]
        else: right = sequence[i:]
        if len(right)>0 and min(right) < root: return False
        leftis,rightis = True,True
        if len(left) > 0:leftis = self.VerifySquenceOfBST(left)
        if len(right) > 0:rightis = self.VerifySquenceOfBST(right)
        return leftis & rightis