class Solution:
    def IsPopOrder(self, pushV, popV):
        temp=[]
        for i in pushV:
            temp.append(i)
            while temp and temp[-1]==popV[0]:
                temp.pop()
                popV.pop(0)
        if not temp:
            return True
        return False
