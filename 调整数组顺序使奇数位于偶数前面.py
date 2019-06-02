class Solution:
    def __init__(self):
        self.odd=[]
        self.evev=[]
    def reOrderArray(self, array):
        for i in array:
            if i%2==0:
                self.evev.append(i)
            else:
                self.odd.append(i)
        return self.odd+self.even