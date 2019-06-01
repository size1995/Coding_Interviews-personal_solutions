class Solution:
    def jumpFloor(self, number):
        a1=1
        a2=2
        if number<3:
            return number
        for i in range(3,number+1):
            a3=a1+a2
            a1=a2
            a2=a3
        return a2