class Solution:
    def rectCover(self, number):
        if number<3:
            return number
        a1=1
        a2=2
        for i in range(3,number+1):
            a3=a1+a2
            a1=a2
            a2=a3
        return a2